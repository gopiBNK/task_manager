from unittest.mock import Base

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class User(Base):
    __tablename__="users"

    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(100))
    email=Column(String(100),unique=True,index=True)
    password=Column(String(225))
    role=Column(String(20),default="Member")

    tasks=relationship("Task",back_populates="assignee")
class Project(Base):
    __tablename__="projects"

    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(100))
    description=Column(String(225))
    created_by=Column(Integer,ForeignKey("users.id"))

    tasks=relationship("Task",back_populates="project")


class Task(Base):
    __tablename__="tasks"
    id =Column(Integer,primary_key=True,index=True)
    title=Column(String(100))
    description=Column(String(225))
    status=Column(String(20),default="ToDo")
    priority=Column(String(20))
    due_date=Column(DateTime)

    assigned_to=Column(Integer,ForeignKey("users.id"))
    project_id=Column(Integer,ForeignKey("projects.id"))

    assignee=relationship("User",back_populates="tasks")
    project=relationship("Project",back_populates="tasks")