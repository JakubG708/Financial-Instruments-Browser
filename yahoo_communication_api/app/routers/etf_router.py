from fastapi import APIRouter
from app.services import yahoo_service

router = APIRouter()

@router.get("/get_etf")
def get_etf():
    return yahoo_service.add(2, 3)
