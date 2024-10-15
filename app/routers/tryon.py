from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import TryOnHistory
import shutil
from PIL import Image

router = APIRouter()

@router.post("/upload-photo/")
async def upload_photo(user_id: int, file: UploadFile = File(...), db: Session = Depends(get_db)):
    file_location = f"static/user_photos/{user_id}_{file.filename}"
    with open(file_location, "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)
    return {"info": f"file '{file.filename}' saved at '{file_location}'"}

@router.post("/try-on/")
def try_on(user_id: int, clothing_item_id: int, db: Session = Depends(get_db)):
    # Fetch user photo and clothing item
    # Implement logic for overlaying clothing item on user photo using Pillow or other libraries
    return {"message": "Try-on simulation in progress"}
