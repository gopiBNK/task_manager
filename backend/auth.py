from passlib.context import CryptContext
from jose import jwt
from datetime import datetime,timedelta

secret_key="secret123"
algorithm="HS256"

pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")

def hash_password(password: str):
    if len(password.encode('utf-8')) > 72:
        raise ValueError("Password too long (max 72 bytes)")
    return pwd_context.hash(password)

def verify_password(plain,hashed):
    return pwd_context.verify(plain,hashed)

def create_token(data: dict):
    to_encode=data.copy()
    expire=datetime.utcnow()+timedelta(hours=2)
    to_encode.update({"exp":expire})
    return jwt.encode(to_encode,secret_key,algorithm=algorithm)

