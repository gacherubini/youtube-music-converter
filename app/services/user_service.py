from sqlalchemy.orm import Session
from sqlalchemy import select
from fastapi import HTTPException
from app.models import User

def create_user(db: Session, *, email: str, password_hash: str) -> User:
    exists = db.scalar(select(User).where(User.email == email))
    if exists:
        raise HTTPException(status_code=400, detail="Email already registered")

    u = User(email=email, password_hash=password_hash)
    db.add(u)
    db.commit()
    db.refresh(u)
    return u

def list_users(db: Session) -> list[User]:
    return db.query(User).all()
