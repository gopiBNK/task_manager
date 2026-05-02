from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

username="root"

password="gopinathv.p02%40"

host="localhost"

database="task_manager"

url=f"mysql+pymysql://{username}:{password}@{host}/{database}"
engine=create_engine(url)

SessionLocal=sessionmaker(bind=engine,autoflush=False,autocommit=False)

Base=declarative_base()