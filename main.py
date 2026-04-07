from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is running successfully!"}

@app.get("/hello")
def say_hello():
    return {"message": "Hello I am Suhasini"}

@app.get("/add")
def add(a: int, b: int):
    return {"result": a + b}

@app.get("/multiply")
def multiply(a: int, b: int):
    return {"result": a * b}

@app.get("/square")
def square(n: int):
    return {
        "operation": "square",
        "input": n,
        "result": n * n
    }