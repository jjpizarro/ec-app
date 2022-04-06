from fastapi import FastAPI
from core import config
from products import router as product_router
from user import router as user_router
from database import models
app = FastAPI(title="Mi App", version="0.0.1")

app.include_router(product_router.api_router)
app.include_router(user_router.api_router)
