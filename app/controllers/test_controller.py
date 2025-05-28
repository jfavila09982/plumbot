import shutil
from fastapi import APIRouter, UploadFile, File, HTTPException
from app.utils.response_helper import reusable_response

from pathlib import Path


router = APIRouter()

@router.get("/test/users")
def get_users():
    users = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"}
    ]
    roles = {
        1: "admin",
        2: "user"
    }
    for user in users:
        user["role"] = roles.get(user["id"],"guest")
    
    return reusable_response(users, message="This is test response")


UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


async def handle_upload(file: UploadFile):
    try:
        file_location = UPLOAD_DIR / file.filename
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        return {"filename": file.filename, "message": "Upload successful"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Route handler
@router.post("/test/upload")
async def upload_file(file: UploadFile = File(...)):
    return await handle_upload(file)