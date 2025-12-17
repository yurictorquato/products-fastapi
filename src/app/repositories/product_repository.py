from uuid import UUID

from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.product_model import ProductModel
from app.schemas.product_schema import ProductRequest, ProductUpdate


class ProductRepository:
    """Camada responsável pela interação direta com o banco de dados."""

    db_session: AsyncSession

    def __init__(self, db_session: AsyncSession) -> None:
        self.db_session = db_session

    async def create_product(self, product_request: ProductRequest) -> ProductModel:
        """Cria e persiste um novo produto no banco de dados."""
        new_product = ProductModel(**product_request.model_dump())

        self.db_session.add(new_product)

        return new_product

    async def get_product_by_id(self, product_id: UUID) -> ProductModel | None:
        """Busca um produto pelo seu ID."""
        product = await self.db_session.execute(
            select(ProductModel).where(ProductModel.id == product_id)
        )

        return product.scalar_one_or_none()

    async def list_all_products(self) -> list[ProductModel]:
        """Lista todos os produtos."""
        products = await self.db_session.execute(select(ProductModel))

        return list(products.scalars().all())

    async def update_product(
        self, product_id: UUID, product_request: ProductUpdate
    ) -> ProductModel | None:
        """Atualiza preço e/ou quantidade de produto existente."""
        update_data = product_request.model_dump(exclude_unset=True)

        if not update_data:
            return None

        product = await self.db_session.execute(
            update(ProductModel)
            .where(ProductModel.id == product_id)
            .values(**update_data)
            .returning(ProductModel)
        )

        return product.scalar_one_or_none()

    async def delete_product(self, product_id: UUID) -> bool:
        """Deleta um produto."""
        product_to_delete = await self.db_session.execute(
            delete(ProductModel)
            .where(ProductModel.id == product_id)
            .returning(ProductModel)
        )

        return bool(product_to_delete.scalar_one_or_none())
