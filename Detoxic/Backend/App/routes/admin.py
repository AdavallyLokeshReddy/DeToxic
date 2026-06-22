from fastapi import APIRouter

router = APIRouter(prefix="/admin")

@router.get("/submissions")
async def all_submissions():
    return []

@router.post("/review/{submission_id}")
async def review_submission(submission_id: int):
    return {"msg": "reviewed"}

@router.get("/stats")
async def admin_stats():
    return {"total_submissions": 0}
