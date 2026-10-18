from fastapi import FastAPI
from starlette.responses import FileResponse
import datetime
import os
import json
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Any


#创建一个用于封装返回值的类
class ApiResponse(BaseModel):
    code: int
    message: str
    data: Any

#为了接收前端返回的json 需要创建一个类
class ChatRequest(BaseModel):
    session_id : str
    message : str

#静态挂载

app = FastAPI(title="Game")
app.mount("/static", StaticFiles(directory="static"), name="static")

#存放历史会话的文件夹
if not os.path.exists('./sessions'):
    os.mkdir('./sessions')

def generate_session_id() -> str:
    return datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

@app.get("/")
def root():
    print("访问项目首页")
    return FileResponse("static/index.html")

@app.post("/api/sessions")
def create_session():
    print("创建新会话")
    session_id = generate_session_id()
    #组装会话信息
    session_data = {
        "current_session": session_id,
        "messages":[]
    }
    with open('./sessions/{}.json'.format(session_id), 'w') as f:
        json.dump(session_data, f,ensure_ascii=False,indent=4)
    # return {
    #     "code" : 200,
    #     "message" : "会话创建成功！",
    #     "data" : session_id
    #
    # }
    return ApiResponse(code=200,message="会话创建成功！",data=session_id)
#   这个接口可以把类对象序列化为字典

@app.post("/api/chat")
def chat(request: ChatRequest):
    #返回的json会封装到类中
    print("与ai交互：{}:{}".format(request.session_id, request.message))
    return ApiResponse(code=200,message="请求成功",data="shuju")




if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

