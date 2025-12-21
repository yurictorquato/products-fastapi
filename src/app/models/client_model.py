from sqlalchemy import String, Integer, CHAR
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base_model import Base


class ClientModel(Base):
    __tablename__ = "tb_client"

    name: Mapped[str] = mapped_column(String(30), nullable=False)
    cpf: Mapped[str] = mapped_column(String(11), unique=True, nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    sex: Mapped[str] = mapped_column(CHAR(length=1), nullable=False)
    address: Mapped[str] = mapped_column(String(50), nullable=False)