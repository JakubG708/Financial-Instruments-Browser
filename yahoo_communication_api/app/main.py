from fastapi import FastAPI
from app.routers import etf_router


app = FastAPI()

app.include_router(etf_router.router, prefix="/etf")
