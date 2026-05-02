from fastapi import APIRouter
from sqlalchemy.orm import Session
from database import SessionLocal
from model import Task
from schemas import TaskCreate

router=APIRouter(prefix="/tasks")

@router.post("/")

def created_task(task:TaskCreate):
    db: Session=SessionLocal()

    new_task=Task(**task.dict())

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return {
        "id": new_task.id,
        "title": new_task.title,
        "message": "Task created successfully"
    }

@router.get("/")
def get_tasks():
    db: Session=SessionLocal()
    return db.query(Task).all()
