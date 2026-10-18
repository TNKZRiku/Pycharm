#FastAPI可以快速开发API接口

from fastapi import FastAPI
app = FastAPI()

#装饰器作用是:接口的访问路径为/ 方式为get
@app.get("/")
def root():
    #此返回值是将要返回的数据
    return {"message": "Hello World"}

@app.get("/user")
def user():
    return [
        {"name": "张三"},
        {"name": "李四"},
        {"name": "王五"},
    ]


if __name__ == "__main__":
    import uvicorn
    #两种运行方式：终端运行或用uvicron的run方法来运行
    uvicorn.run(app, host="127.0.0.1", port=8000)
