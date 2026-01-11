from datetime import datetime

from sqlalchemy import CHAR, Integer, String, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base_model import Base


class ClientModel(Base):
    """Modelo de Cliente para persistência no banco de dados"""

    __tablename__ = "tb_clients"

    name: Mapped[str] = mapped_column(String(30), nullable=False)
    cpf: Mapped[str] = mapped_column(String(11), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    sex: Mapped[str] = mapped_column(CHAR(length=1), nullable=False)
    address: Mapped[str] = mapped_column(String(50), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
