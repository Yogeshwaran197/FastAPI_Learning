from fastapi import APIRouter
from src.utils.utils import get_all_porduct

productRoutes = APIRouter()


@productRoutes.get("/get_products")
def getAllProducts():
    return get_all_porduct()

@productRoutes.post("/create_products")
def creatProducts():
    return