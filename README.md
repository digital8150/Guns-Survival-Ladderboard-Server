# Guns Survival Online Leaderboard Backend

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.111.0-009688?style=for-the-badge&logo=fastapi)
![Uvicorn](https://img.shields.io/badge/Uvicorn-0.30.1-F76900?style=for-the-badge&logo=uvicorn)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite)

A simple yet robust backend server for the Guns Survival online leaderboard, built with FastAPI and utilizing SQLite for data persistence. This project provides essential API endpoints for managing player scores, including adding new entries, retrieving top scores, and querying scores around a specific player.

## ✨ Features

-   **Comprehensive Score Data:** Each score entry includes a unique ID, registration timestamp, score value, survival time, and player nickname.
-   **Top 10 Leaderboard:** Easily retrieve the top 10 highest scores.
-   **Score Submission:** API endpoint for players to submit their scores.
-   **Contextual Score Retrieval:** Fetch scores around a specific player's entry, providing context within the leaderboard.
-   **Score Deletion:** Ability to remove individual score entries.
-   **Leaderboard Reset:** Option to clear all scores from the leaderboard.
-   **Data Persistence:** All score data is stored persistently using SQLite, ensuring data is not lost upon server restarts.

## 🚀 Technology Stack

-   **Python**: The core programming language.
-   **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.
-   **Pydantic**: Used for data validation and settings management, ensuring robust and type-safe API requests and responses.
-   **SQLite**: A lightweight, file-based relational database, perfect for simple, embedded data storage without the need for a separate database server.
-   **Uvicorn**: An ASGI server, powering the FastAPI application for asynchronous operations.

## ⚡ Quick Start

Follow these steps to get the leaderboard server up and running on your local machine or prepare it for deployment.

### Prerequisites

-   Python 3.9+ (Recommended)
-   `pip` (Python package installer)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/guns-survival-online-ladder-board.git # Replace with your actual repo URL
    cd guns-survival-online-ladder-board
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Running the Server

To start the FastAPI server:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

The server will be accessible at `http://localhost:8000`.

### API Documentation

Once the server is running, you can access the interactive API documentation (Swagger UI) at:

[http://localhost:8000/docs](http://localhost:8000/docs)

### Deployment on ARM Linux

Deploying to an ARM Linux server (e.g., Raspberry Pi, AWS Graviton) involves similar steps:

1.  **Install Python and pip:** Ensure Python 3.9+ and pip are installed on your ARM Linux machine.
    ```bash
    sudo apt update
    sudo apt install python3 python3-pip
    ```
2.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/guns-survival-online-ladder-board.git # Replace with your actual repo URL
    cd guns-survival-online-ladder-board
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the server:** You might want to use a process manager like `systemd` or `supervisor` for production environments to keep the server running reliably.
    ```bash
    uvicorn main:app --host 0.0.0.0 --port 8000
    ```

## 📚 API Endpoints

Here's a brief overview of the available API endpoints:

-   **`GET /`**
    -   Returns a welcome message.

-   **`GET /leaderboard/top10`**
    -   Retrieves the top 10 scores from the leaderboard, sorted by score in descending order.

-   **`POST /leaderboard`**
    -   Submits a new score entry to the leaderboard.
    -   **Request Body:**
        ```json
        {
            "score": 12345,
            "survival_time": 300,
            "nickname": "PlayerOne"
        }
        ```

-   **`GET /leaderboard/{score_id}/around`**
    -   Retrieves 10 score entries around a specific `score_id` (4 before, the target ID, and 5 after), sorted by score.

-   **`DELETE /leaderboard/{score_id}`**
    -   Deletes a specific score entry from the leaderboard using its `score_id`.

-   **`DELETE /leaderboard`**
    -   Resets the entire leaderboard, deleting all score entries.

---

_Developed with ❤️ by Your Name/Team_ # Replace with your name or team name
