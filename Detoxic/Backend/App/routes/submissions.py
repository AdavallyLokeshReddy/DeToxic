from fastapi import APIRouter, Depends, HTTPException
from typing import List
from ..database.connection import get_db
from ..database import crud
from sqlalchemy.orm import Session

router = APIRouter(prefix="/submissions")

@router.get("/")
async def get_submissions(db: Session = Depends(get_db)):
    return crud.list_submissions(db)

@router.post("/")
async def create_submission(payload: dict, db: Session = Depends(get_db)):
    try:
        sub = crud.create_submission(db, comment_text=payload.get('comment_text'))
        return {"id": sub.id, "comment_text": sub.comment_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{submission_id}")
async def get_submission(submission_id: int, db: Session = Depends(get_db)):
    sub = crud.get_submission(db, submission_id)
    if not sub:
        raise HTTPException(status_code=404)
    return {"id": sub.id, "comment_text": sub.comment_text}

@router.delete("/{submission_id}")
async def delete_submission(submission_id: int, db: Session = Depends(get_db)):
    # stub - implement proper delete
    return {"msg": "deleted"}
