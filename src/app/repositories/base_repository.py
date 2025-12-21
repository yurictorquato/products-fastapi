from typing import TypeVar, Generic, Type
from uuid import UUID

from pydantic import BaseModel
from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.base_model import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

class BaseRepository(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    """Repository genérico com operações CRUD básicas."""

    def __init__(self, model: Type[ModelType], db_session: AsyncSession) -> None:
        self.model = model
        self.db_session = db_session

    async def save(self, schema: CreateSchemaType) -> ModelType:
        """Cria e persiste uma nova entidade no banco de dados."""
        new_entity = self.model(**schema.model_dump())
        self.db_session.add(new_entity)

        return new_entity

    async def find_by_id(self, entity_id: UUID) -> ModelType | None:
        """Busca uma entidade pelo seu ID."""
        result = await self.db_session.execute(select(self.model).where(self.model.id == entity_id))

        return result.scalar_one_or_none()

    async def find_all(self) -> list[ModelType]:
        """Lista todas as entidades."""
        result = await self.db_session.execute(select(self.model))

        return list(result.scalars().all())

    async def update(self, entity_id: UUID, schema: UpdateSchemaType) -> ModelType | None:
        """Atualiza uma entidade existente."""
        update_data = schema.model_dump(exclude_unset=True)

        if not update_data:
            return None

        result = await self.db_session.execute(
            update(self.model)
            .where(self.model.id == entity_id)
            .values(**update_data)
            .returning(self.model)
        )

        return result.scalar_one_or_none()

    async def delete(self, entity_id: UUID) -> bool:
        """Deleta uma entidade."""
        result = await self.db_session.execute(
            delete(self.model)
            .where(self.model.id == entity_id)
            .returning(self.model)
        )

        return bool(result.scalar_one_or_none())
