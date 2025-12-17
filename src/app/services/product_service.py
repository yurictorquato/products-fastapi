from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.product_model import ProductModel
from app.repositories.product_repository import ProductRepository
from app.schemas.product_schema import ProductRequest, ProductUpdate


class ProductService:
    """Camada responsável pela lógica de negócio dos produtos."""

    repository: ProductRepository

    def __init__(self, db_session: AsyncSession) -> None:
        self.repository = ProductRepository(db_session)

    async def create_product(self, product_request: ProductRequest) -> ProductModel:
        """Cria um novo produto."""
        return await self.repository.create_product(product_request)

    async def get_product_by_id(self, product_id: UUID) -> ProductModel | None:
        """Busca um produto pelo ID."""
        return await self.repository.get_product_by_id(product_id)

    async def list_all_products(self) -> list[ProductModel]:
        """Lista todos os produtos."""
        return await self.repository.list_all_products()

    async def update_product(
        self, product_id: UUID, product_request: ProductUpdate
    ) -> ProductModel | None:
        """Atualiza um produto existente."""
        return await self.repository.update_product(product_id, product_request)

    async def delete_product(self, product_id: UUID) -> bool:
        """Deleta um produto pelo ID."""
        return await self.repository.delete_product(product_id)
