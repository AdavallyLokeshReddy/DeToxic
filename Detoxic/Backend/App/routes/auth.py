from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/auth")

class RegisterIn(BaseModel):
    username: str
    email: str
    password: str

@router.post("/register")
async def register(payload: RegisterIn):
    return {"msg": "register endpoint (stub)"}
