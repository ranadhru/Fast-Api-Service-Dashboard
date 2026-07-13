from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.database import Base, engine
from app.services.health import get_health_status
from app.logger import logger

# NEW IMPORT
from prometheus_fastapi_instrumentator import Instrumentator

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Service Dashboard",
    version="1.0.0"
)

# NEW: Enable Prometheus Metrics
Instrumentator().instrument(app).expose(app)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")


@app.get("/")
async def home(request: Request):
    logger.info("Home page accessed")
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )


@app.get("/health")
async def health():
    logger.info("Health endpoint called")
    return get_health_status()