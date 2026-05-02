from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from model import User
from schemas import UserCreate,UserLogin
from auth import hash_password,verify_password,create_token

router=APIRouter()

@router.post("/signup")
def signup(user: UserCreate):
    db:Session=SessionLocal()

    existing=db.query(User).filter(User.email==user.email).first()
    if existing:
        raise HTTPException(status_code=400,detail="Email already exists")
    new_user=User(
        name=user.name,
        email=user.email,
        password=hash_password(user.password)
    )
    db.add(new_user)
    db.commit()

    return {"message": "User created"}
@router.post("/login")
def login(user: UserLogin):
    db:Session=SessionLocal()

    db_user=db.query(User).filter(User.email==user.email).first()
    if not db_user:
        raise HTTPException(status_code=400,detail="Invalid credentials")
    if not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=400,detail="Invalid credentials")

    token=create_token({"user_id":db_user.id,"role":db_user.role})
    return {"access_token": token}
