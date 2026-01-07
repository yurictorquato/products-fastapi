from app.exceptions.exceptions import ProductNotFoundException
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.product_repository import ProductRepository
from app.schemas.product_schema import ProductRequest, ProductUpdate, ProductResponse


class ProductService:
    """Camada responsável pela lógica de negócio dos produtos."""

    def __init__(self, db_session: AsyncSession) -> None:
        self.repository: ProductRepository = ProductRepository(db_session)

    async def create_product(self, product_request: ProductRequest) -> ProductResponse:
        """Cria um produto."""
        product_model = await self.repository.save(product_request)

        return ProductResponse.model_validate(product_model)

    async def get_product_by_id(self, product_id: UUID) -> ProductResponse:
        """Busca um produto pelo ID."""
        product_model = await self.repository.find_by_id(product_id)

        if not product_model:
            raise ProductNotFoundException(product_id)

        return ProductResponse.model_validate(product_model)

    async def list_all_products(self) -> list[ProductResponse]:
        """Lista todos os produtos."""
        products_model = await self.repository.find_all()

        return [ProductResponse.model_validate(product) for product in products_model]

    async def update_product(
        self, product_id: UUID, product_request: ProductUpdate
    ) -> ProductResponse:
        """Atualiza um produto existente."""
        product_model = await self.repository.update(product_id, product_request)

        if not product_model:
            raise ProductNotFoundException(product_id)

        return ProductResponse.model_validate(product_model)

    async def delete_product(self, product_id: UUID) -> None:
        """Deleta um produto pelo ID."""
        deleted = await self.repository.delete(product_id)

        if not deleted:
            raise ProductNotFoundException(product_id)
