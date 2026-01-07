from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.core.database import get_db_session
from app.schemas.product_schema import ProductRequest, ProductResponse, ProductUpdate
from app.services.product_service import ProductService

router = APIRouter()


def get_product_service(
    db_session: AsyncSession = Depends(get_db_session),
) -> ProductService:
    """Dependency para injetar o ProductService."""
    return ProductService(db_session)


@router.post(
    path="/",
    summary="Cria um novo produto",
    description="Cria um novo produto com nome, preço e quantidade",
    status_code=status.HTTP_201_CREATED,
    response_model=ProductResponse,
)
async def create_product(
    product_request: ProductRequest,
    service: ProductService = Depends(get_product_service),
):
    """Cria um novo produto."""
    return await service.create_product(product_request)


@router.get(
    path="/{product_id}",
    summary="Consulta um produto pelo ID",
    description="Retorna os dados de um produto específico pelo seu ID",
    status_code=status.HTTP_200_OK,
    response_model=ProductResponse,
)
async def get_product_by_id(
    product_id: UUID,
    service: ProductService = Depends(get_product_service),
):
    """Busca um produto pelo ID."""
    return await service.get_product_by_id(product_id)


@router.get(
    path="/",
    summary="Consulta todos os produtos",
    description="Retorna uma lista com todos os produtos cadastrados",
    status_code=status.HTTP_200_OK,
    response_model=list[ProductResponse],
)
async def list_all_products(service: ProductService = Depends(get_product_service)):
    """Lista todos os produtos."""
    return await service.list_all_products()


@router.patch(
    path="/{product_id}",
    summary="Atualiza um produto pelo ID",
    description="Atualiza o preço e/ou a quantidade de um produto existente",
    status_code=status.HTTP_200_OK,
    response_model=ProductResponse,
)
async def update_product(
    product_id: UUID,
    product_update: ProductUpdate,
    service: ProductService = Depends(get_product_service),
):
    """Atualiza preço e/ou quantidade de um produto."""
    return await service.update_product(product_id, product_update)


@router.delete(
    path="/{product_id}",
    summary="Deleta um produto pelo ID",
    description="Remove um produto do sistema pelo seu ID",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_product(
    product_id: UUID, service: ProductService = Depends(get_product_service)
):
    """Deleta um produto."""
    await service.delete_product(product_id)
