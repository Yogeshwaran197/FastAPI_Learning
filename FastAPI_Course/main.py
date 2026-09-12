from fastapi import FastAPI

app =  FastAPI(
    title="FastAPI Coruse"
)

@app.get("/yogesh")
def greet():
    return "Hello i am yogesh"


###CRUD APIs