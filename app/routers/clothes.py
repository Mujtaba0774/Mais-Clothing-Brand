from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import ClothingItem

router = APIRouter()

@router.get("/clothes/")
def get_clothing_items(db: Session = Depends(get_db)):
    clothes = db.query(ClothingItem).all()
    return clothes
