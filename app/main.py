from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.database import Base, engine
from app.services.health import get_health_status
from app.logger import logger

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Service Dashboard",
    version="1.0.0"
)

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


from app.services.health import get_health_status

@app.get("/health")
async def health():
    logger.info("Health endpoint called")
    return get_health_status()