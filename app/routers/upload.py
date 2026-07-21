import os
from fastapi import APIRouter, UploadFile, File

from services.document_loader import(
    load_pdf,
    split_text
)
from services.rag import(
    store_chunks
)

router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)

UPLOAD_DIR= "uploads"

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)

@router.post("/")
async def upload_document(file: UploadFile= File(...)):
    file_path = f"{UPLOAD_DIR}/{file.filename}"

    with open(
        file_path,
        "wb"
    ) as buffer:
        buffer.write(
            await file.read()
        )
    
    text = load_pdf(file_path)

    chunks = split_text(
        text
    )

    store_chunks(
        chunks,
        file.filename
    )

    return{
        "filename": file.filename,
        "chunk_created": len(chunks),
        "status": "processed"
    }