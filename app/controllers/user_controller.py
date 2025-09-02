from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app.services.user_service import create_user as create_user_svc, list_users as list_users_svc

router = APIRouter(prefix="/users", tags=["users"])

@router.post("")
def create_user(email: str, password_hash: str, db: Session = Depends(get_db)):
    u = create_user_svc(db, email=email, password_hash=password_hash)
    return {"id": str(u.id), "email": u.email}

@router.get("")
def list_users(db: Session = Depends(get_db)):
    rows = list_users_svc(db)
    return [{"id": str(u.id), "email": u.email} for u in rows]
