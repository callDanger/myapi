from fastapi import FastAPI

# 创建 FastAPI 实例
app = FastAPI()

# 测试接口
@app.get("/")
def home():
    return {"message": "FastAPI 服务运行成功！"}

# 测试带参数的接口
@app.get("/user/{name}")
def get_user(name: str):
    return {"欢迎你": name}