from fastapi import APIRouter

from app.controllers.product_controller import router as products

api_router = APIRouter()

api_router.include_router(router=products, prefix="/products", tags=["products"])
