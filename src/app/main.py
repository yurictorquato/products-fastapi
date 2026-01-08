from fastapi import FastAPI

from app.exceptions import InvalidProductDataException, ProductNotFoundException
from app.handlers import (
    invalid_product_data_exception_handler,
    product_not_found_exception_handler,
)
from app.routers import api_router

app = FastAPI(
    title="Products FastAPI", description="API para gerenciamento de produtos"
)

app.add_exception_handler(ProductNotFoundException, product_not_found_exception_handler)
app.add_exception_handler(
    InvalidProductDataException, invalid_product_data_exception_handler
)

app.include_router(api_router)