#### 1. 파이썬 이미지로 시작 (Python 3.10 버전 사용)
FROM python:3.10-slim

# 2. 작업 디렉토리 설정 (애플리케이션 파일들이 위치할 곳)
WORKDIR /app

# 3. requirements.txt를 복사하고 의존성 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. 애플리케이션 코드 복사
COPY . /app

# 5. 컨테이너 실행 시 uvicorn을 통해 FastAPI 서버 실행 (예시: main.py 파일에 FastAPI 서버가 있다면)
CMD ["fastapi","run", "main.py"]