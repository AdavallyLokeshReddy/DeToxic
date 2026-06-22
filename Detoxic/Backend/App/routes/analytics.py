from fastapi import APIRouter

router = APIRouter(prefix="/analytics")

@router.get("/stats")
async def stats():
    return {"total_submissions": 0}

@router.get("/history")
async def history():
    return []

@router.get("/trends")
async def trends():
    return {"trend": []}
