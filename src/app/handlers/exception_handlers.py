from fastapi import Request
from fastapi.responses import JSONResponse
from starlette import status

from app.exceptions import InvalidProductDataException, ProductNotFoundException


async def product_not_found_exception_handler(
    request: Request, exception: ProductNotFoundException
) -> JSONResponse:
    """Handler para quando o produto não é encontrado."""
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"detail": exception.message, "product_id": exception.product_id},
    )


async def invalid_product_data_exception_handler(
    request: Request, exception: InvalidProductDataException
) -> JSONResponse:
    """Handler para dados inválidos."""
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
        content={"detail": exception.message},
    )
