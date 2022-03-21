from fastapi import FastAPI
from core.config import settings
from database import models
from products import router as product_router


app = FastAPI(title="My application", version="0.1")


@app.get("/")
async def home() -> dict:
    return {'message': 'OK'}

app.include_router(product_router.api_router)

