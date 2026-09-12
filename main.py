from fastapi import FastAPI
from src.routes.productroute import productRoutes

app =  FastAPI(
    title="FastAPI Coruse"
)

@app.get("/yogesh")
def greet():
    return "Hello i am yogesh"


app.include_router(productRoutes)

###CRUD APIs - Products - JSON file

