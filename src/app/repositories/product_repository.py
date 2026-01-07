from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.product_model import ProductModel
from app.repositories.base_repository import BaseRepository
from app.schemas.product_schema import ProductRequest, ProductUpdate


class ProductRepository(BaseRepository[ProductModel, ProductRequest, ProductUpdate]):
    """Repository de produtos com métodos específicos adicionais."""

    def __init__(self, db_session: AsyncSession) -> None:
        super().__init__(ProductModel, db_session)

    async def find_by_name(self, name: str) -> ProductModel | None:
        """Busca um produto pelo nome."""
        result = await self.db_session.execute(select(ProductModel).where(ProductModel.name == name))

        return result.scalar_one_or_none()
