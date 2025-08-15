# Guns Survival 온라인 리더보드 백엔드

FastAPI를 사용하여 구축하고 SQLite를 활용하는 Guns Survival 온라인 리더보드를 위한 간단한 백엔드 서버입니다. 이 프로젝트는 새로운 항목 추가, 상위 점수 검색, 특정 플레이어 주변의 점수 조회 등 플레이어 점수 관리를 위한 필수적인 API 엔드포인트를 제공합니다.

## ✨ 기능 (Features)

  - **포괄적인 점수 데이터:** 각 점수 항목에는 고유 ID, 등록 타임스탬프, 점수 값, 생존 시간, 플레이어 닉네임이 포함됩니다.
  - **상위 10위 리더보드:** 가장 높은 점수 상위 10개를 쉽게 가져옵니다.
  - **점수 제출:** 플레이어가 자신의 점수를 제출할 수 있는 API 엔드포인트입니다.
  - **맥락적 점수 검색:** 특정 플레이어의 항목 주변 점수를 가져와 리더보드 내에서 맥락을 제공합니다.
  - **점수 삭제:** 개별 점수 항목을 제거하는 기능입니다.
  - **리더보드 초기화:** 리더보드의 모든 점수를 지우는 옵션입니다.
  - **데이터 영속성:** 모든 점수 데이터는 서버 재시작 시에도 손실되지 않도록 SQLite를 사용하여 지속적으로 저장됩니다.

## 🚀 기술 스택 (Technology Stack)

  - **Python**: 핵심 프로그래밍 언어입니다.
  - **FastAPI**: 표준 Python 타입 힌트를 기반으로 Python 3.7+에서 API를 구축하기 위한 현대적이고 빠른(고성능) 웹 프레임워크입니다.
  - **Pydantic**: 데이터 유효성 검사 및 설정 관리에 사용되어 강력하고 type-safe한 API 요청 및 응답을 보장합니다.
  - **SQLite**: 별도의 데이터베이스 서버 없이도 간단하고 내장된 데이터 저장에 완벽한 경량 파일 기반 관계형 데이터베이스입니다.
  - **Uvicorn**: 비동기 작업을 위해 FastAPI 애플리케이션에 전력을 공급하는 ASGI 서버입니다.

## ⚡ 빠른 시작 (Quick Start)

로컬 머신에서 리더보드 서버를 실행하거나 배포를 위해 준비하려면 다음 단계를 따르세요.

### 전제 조건 (Prerequisites)

  - Python 3.9+ (권장)
  - `pip` (Python 패키지 설치 프로그램)

### 설치 (Installation)

1.  **저장소(repository) 복제:**
    ```bash
    git clone https://github.com/your-username/guns-survival-online-ladder-board.git # 실제 저장소 URL로 교체하세요
    cd guns-survival-online-ladder-board
    ```
2.  **의존성 설치:**
    ```bash
    pip install -r requirements.txt
    ```

### 서버 실행 (Running the Server)

FastAPI 서버를 시작하려면:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

서버는 `http://localhost:8000`에서 접근할 수 있습니다.

### API 문서 (API Documentation)

서버가 실행되면 다음 주소에서 대화형 API 문서(Swagger UI)에 액세스할 수 있습니다.

[http://localhost:8000/docs](https://www.google.com/search?q=http://localhost:8000/docs)

### ARM Linux에 배포 (Deployment on ARM Linux)

ARM Linux 서버(예: Raspberry Pi, AWS Graviton)에 배포하는 과정은 비슷한 단계를 따릅니다. Oracle Cloud Infrasturcture 가 제공하는 무료티어 ARM Linux VM에서도 잘 동작합니다.

1.  **Python 및 pip 설치:** ARM Linux 머신에 Python 3.9+ 및 pip가 설치되어 있는지 확인하세요.
    ```bash
    sudo apt update
    sudo apt install python3 python3-pip
    ```
2.  **저장소 복제:**
    ```bash
    git clone https://github.com/your-username/guns-survival-online-ladder-board.git # 실제 저장소 URL로 교체하세요
    cd guns-survival-online-ladder-board
    ```
3.  **의존성 설치:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **서버 실행:** 프로덕션 환경에서는 서버를 안정적으로 실행하기 위해 `systemd` 또는 `supervisor`와 같은 프로세스 관리자를 사용하는 것이 좋습니다.
    ```bash
    uvicorn main:app --host 0.0.0.0 --port 8000
    ```

## 📚 API 엔드포인트 (API Endpoints)

사용 가능한 API 엔드포인트에 대한 간략한 개요입니다.

  - **`GET /`**

      - 환영 메시지를 반환합니다.

  - **`GET /leaderboard/top10`**

      - 리더보드에서 상위 10개 점수를 내림차순으로 정렬하여 가져옵니다.

  - **`POST /leaderboard`**

      - 리더보드에 새로운 점수 항목을 제출합니다.
      - **요청 본문 (Request Body):**
        ```json
        {
          "score": 12345,
          "survival_time": 300,
          "nickname": "PlayerOne"
        }
        ```

  - **`GET /leaderboard/{score_id}/around`**

      - 특정 `score_id` 주변의 점수 항목 10개(대상 ID 이전 4개, 대상 ID, 이후 5개)를 점수 순으로 정렬하여 가져옵니다.

  - **`DELETE /leaderboard/{score_id}`**

      - `score_id`를 사용하여 리더보드에서 특정 점수 항목을 삭제합니다.

  - **`DELETE /leaderboard`**

      - 전체 리더보드를 초기화하고 모든 점수 항목을 삭제합니다.

-----

*Developed with ❤️ by Your Name/Team* \# 이름 또는 팀 이름으로 교체하세요
