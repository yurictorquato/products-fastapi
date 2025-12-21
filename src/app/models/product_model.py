from sqlalchemy import Float, Integer, String
from sqlalchemy.orm import mapped_column, Mapped

from app.models.base_model import Base


class ProductResponse(Base):
    __tablename__ = "tb_produtos"

    name: Mapped[str] = mapped_column(String(25), nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
