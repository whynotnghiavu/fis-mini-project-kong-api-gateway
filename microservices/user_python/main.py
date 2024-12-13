import settings
import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger


from app.user.routers.user import user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Server is starting...")
    yield
    logger.info("Server is shutting down...")


app = FastAPI(
    lifespan=lifespan,
    title=f"{settings.NAME_SERVICE}",
    openapi_url=f"/api/{settings.NAME_SERVICE}/openapi.json",
    docs_url=f"/api/{settings.NAME_SERVICE}/docs",
    redoc_url=f"/api/{settings.NAME_SERVICE}/redoc",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(user_router, prefix=f"/api/{settings.NAME_SERVICE}")


@app.get(f"/api/{settings.NAME_SERVICE}")
async def root():
    return {
        'language': f'python',
        'message': f'Hello World from {settings.NAME_SERVICE}'
    }


if __name__ == "__main__":
    logger.info(f"Starting application with FASTAPI_ENVIRONMENT={settings.FASTAPI_ENVIRONMENT}")

    if settings.FASTAPI_ENVIRONMENT == "DEVELOPMENT":
        uvicorn.run("main:app", host=settings.SERVER_IP, port=settings.SERVER_PORT, reload=True)
    else:
        uvicorn.run("main:app", host=settings.SERVER_IP, port=settings.SERVER_PORT)
