from datetime import datetime
from sqlalchemy import text
import time

from app.database import SessionLocal
from app.redis_client import redis_client


def get_health_status():

    start = time.perf_counter()

    db_status = "Disconnected"
    redis_status = "Disconnected"

    try:
        db = SessionLocal()
        db.execute(text("SELECT 1"))
        db.close()
        db_status = "Connected"
    except Exception:
        pass

    try:
        redis_client.ping()
        redis_status = "Connected"
    except Exception:
        pass

    end = time.perf_counter()

    response_time = round((end - start) * 1000, 2)

    return {
        "status": "Healthy",
        "database": db_status,
        "redis": redis_status,
        "version": "1.0.0",
        "environment": "Production",
        "server_time": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        "response_time": f"{response_time} ms"
    }