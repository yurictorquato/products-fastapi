from sqlalchemy.ext.asyncio import AsyncSession

from app.models.client_model import ClientModel
from app.repositories.base_repository import BaseRepository
from app.schemas.client_schema import ClientRequest, ClientUpdate


class ClientRepository(BaseRepository[ClientModel, ClientRequest, ClientUpdate]):

    def __init__(self, db_session: AsyncSession) -> None:
        super().__init__(ClientModel, db_session)
