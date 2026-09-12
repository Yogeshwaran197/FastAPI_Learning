from anyio.itertools import product
from h11._abnf import status_code
from fastapi.exceptions import HTTPException
from fastapi import APIRouter
from  src.utils.utils import get_all_product

productRoutes = APIRouter()


@productRoutes.get("/get_products")
def getAllProducts(product_id: int = None):
    
    all_product = getAllProducts()

    if not product_id:
        return all_product
    
    for product in all_product:
        if product['id'] == product_id:
            return product
            
    return HTTPException(
        status_code = 400,
        detail = {"erro, id not found"}
    )

    

@productRoutes.get("/{id}")
def getOneProduct(id:int):
    allProducts = get_all_product

    for product in allProducts():
        if product['id'] == id:
            return product
    return HTTPException(
        status_code = 400,
        detail = {"erro, id not found"}
    )

@productRoutes.post("/create_products")
def creatProducts():
    return