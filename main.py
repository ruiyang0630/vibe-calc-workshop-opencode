from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root():
    return FileResponse('static/index.html')

@app.get("/add/{a}/{b}")
def add(a: int, b: int):
    # ❌ [BUG] 邏輯壞了，回傳 0
    return {"result": 0}

@app.get("/multiply/{a}/{b}")
def multiply(a: int, b: int):
    # ❌ [BUG] 尚未實作
    return {"result": 0}
