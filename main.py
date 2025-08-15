from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Dict, Optional
import uuid
import datetime
import sqlite3

app = FastAPI()

DATABASE_URL = "leaderboard.db"

def get_db():
    conn = sqlite3.connect(DATABASE_URL)
    conn.row_factory = sqlite3.Row # This allows accessing columns by name
    try:
        yield conn
    finally:
        conn.close()

def create_table(db: sqlite3.Connection):
    cursor = db.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS scores (
            id TEXT PRIMARY KEY,
            registration_date TEXT,
            score INTEGER,
            survival_time INTEGER,
            nickname TEXT
        )
    """)
    db.commit()

@app.on_event("startup")
def startup_event():
    conn = sqlite3.connect(DATABASE_URL)
    create_table(conn)
    conn.close()

class ScoreEntry(BaseModel):
    id: str
    registration_date: datetime.datetime
    score: int
    survival_time: int
    nickname: str

class ScoreCreate(BaseModel):
    score: int
    survival_time: int
    nickname: str

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Guns Survival Online Leaderboard API!"}

@app.get("/leaderboard/top10", response_model=List[ScoreEntry])
async def get_top_10_leaderboard(db: sqlite3.Connection = Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM scores ORDER BY score DESC LIMIT 10")
    rows = cursor.fetchall()
    return [ScoreEntry(**row) for row in rows]

@app.post("/leaderboard", response_model=ScoreEntry)
async def add_score(score_data: ScoreCreate, db: sqlite3.Connection = Depends(get_db)):
    new_id = str(uuid.uuid4())
    registration_date_utc = datetime.datetime.now(datetime.timezone.utc)
    
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO scores (id, registration_date, score, survival_time, nickname) VALUES (?, ?, ?, ?, ?)",
        (new_id, registration_date_utc.isoformat(), score_data.score, score_data.survival_time, score_data.nickname)
    )
    db.commit()
    
    return ScoreEntry(
        id=new_id,
        registration_date=registration_date_utc,
        score=score_data.score,
        survival_time=score_data.survival_time,
        nickname=score_data.nickname
    )

@app.get("/leaderboard/{score_id}/around", response_model=List[ScoreEntry])
async def get_leaderboard_around_id(score_id: str, db: sqlite3.Connection = Depends(get_db)):
    cursor = db.cursor()
    
    # Get the score of the target ID to find its rank
    cursor.execute("SELECT score FROM scores WHERE id = ?", (score_id,))
    target_score_row = cursor.fetchone()
    if not target_score_row:
        raise HTTPException(status_code=404, detail="Score ID not found")
    
    target_score = target_score_row["score"]

    # Get all scores sorted by score
    cursor.execute("SELECT * FROM scores ORDER BY score DESC")
    all_scores = [ScoreEntry(**row) for row in cursor.fetchall()]

    try:
        # Find the index of the given score_id in the sorted list
        target_index = -1
        for i, entry in enumerate(all_scores):
            if entry.id == score_id:
                target_index = i
                break

        if target_index == -1: # Should not happen if target_score_row was found
            raise HTTPException(status_code=404, detail="Score ID not found in sorted list")

        # Calculate start and end indices for the 10 entries (4 before, 1 target, 5 after)
        start_index = max(0, target_index - 4)
        end_index = min(len(all_scores), target_index + 5 + 1) # +1 because slice is exclusive

        # Adjust if not enough elements before or after
        if end_index - start_index < 10:
            if start_index == 0: # Not enough before, take more from after
                end_index = min(len(all_scores), start_index + 10)
            elif end_index == len(all_scores): # Not enough after, take more from before
                start_index = max(0, end_index - 10)

        return all_scores[start_index:end_index]

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/leaderboard/{score_id}")
async def delete_score(score_id: str, db: sqlite3.Connection = Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("DELETE FROM scores WHERE id = ?", (score_id,))
    db.commit()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Score ID not found")
    return {"message": f"Score with ID {score_id} deleted successfully."}

@app.delete("/leaderboard")
async def reset_leaderboard(db: sqlite3.Connection = Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("DELETE FROM scores")
    db.commit()
    return {"message": "Leaderboard has been reset."}

