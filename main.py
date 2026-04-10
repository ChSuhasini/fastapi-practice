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

@app.get("/fibonacci")
def fibonacci(n: int):
    if n < 0:
        return {"error": "Input must be a non-negative integer."}
    elif n == 0:
        return {"result": 0}
    elif n == 1:
        return {"result": 1}
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return {"result": b}

