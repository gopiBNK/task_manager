from pydantic import BaseModel
from datetime import datetime

class UserCreate(BaseModel):
    name:str
    email:str
    password:str

class UserLogin(BaseModel):
    email:str
    password:str

class ProjectCreate(BaseModel):
    name:str
    description:str

class TaskCreate(BaseModel):
    title:str
    description:str
    priority:str
    due_date:datetime
    assigned_to:int
    project_id:int
    