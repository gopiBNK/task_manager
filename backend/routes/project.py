from fastapi import APIRouter
from sqlalchemy.orm import Session
from database import SessionLocal
from model import Project
from schemas import ProjectCreate


router=APIRouter(prefix="/projects")

@router.post("/")
def create_project(project: ProjectCreate):
    db: Session=SessionLocal()

    new_project=Project(
        name=project.name,
        description=project.description,
        created_by=1
    )
    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    return {
        "id": new_project.id,
        "name": new_project.name,
        "description": new_project.description
    }
@router.get("/")
def get_projects():
    db: Session=SessionLocal()
    return db.query(Project).all()
