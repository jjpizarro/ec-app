from fastapi import FastAPI
from app.products import router as product_router
from app.user import router as user_router
from app.auth import router as auth_router

from app.database import models

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Mi App", version="0.0.1")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.include_router(product_router.api_router)
app.include_router(user_router.api_router)
app.include_router(auth_router.api_router)
