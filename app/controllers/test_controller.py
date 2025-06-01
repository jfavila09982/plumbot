import shutil
from fastapi import APIRouter, UploadFile, File, HTTPException
from app.utils.response_helper import reusable_response
from PyPDF2 import PdfReader
import io

from pathlib import Path

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

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


def extract_text_from_pdf(pdf_file):
    pdf_reader = PdfReader(io.BytesIO(pdf_file))
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text    
    



#upload files 
#-------------------------------------------
async def handle_upload(file: UploadFile):
    try:
        file_location = UPLOAD_DIR / file.filename
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        if file.filename.lower().endswith('.pdf'):
            pdf_reader = PdfReader(file_location)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            
            prompt = f"The PDF file contains the following text: {text[:500]}..." 
            return {"filename": file.filename, "message": "Upload successful", "prompt": prompt}
        else:
            return {"filename": file.filename, "message": "Upload successful, but file is not a PDF"}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Route handler
@router.post("/test/upload")
async def upload_file(file: UploadFile = File(...)):
    return await handle_upload(file)
#-------------------------------------------





