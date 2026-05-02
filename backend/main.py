from fastapi import FastAPI
from database import Base,engine
from routes import user,project,task

app =FastAPI()

Base.metadata.create_all(bind=engine)
app.include_router(user.router)
app.include_router(project.router)
app.include_router(task.router)

@app.get("/")
def home():
    return {"message": "API running"}
