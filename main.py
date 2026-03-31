from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
import models
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


class UserCreate(BaseModel):
    name: str


# 测试接口
@app.get("/")
def home():
    return {"message": "FastAPI 服务运行成功！"}


# 测试带参数的接口
@app.get("/user/{name}")
def get_user(name: str):
    return {"欢迎你": name}


# 新增用户接口
@app.post("/set_user")
def set_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"id": db_user.id, "name": db_user.name}
