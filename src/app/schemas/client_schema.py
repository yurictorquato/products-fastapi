from typing import Annotated
from uuid import UUID

from pydantic import Field, PositiveInt

from app.schemas.base_schema import BaseSchema


class ClientRequest(BaseSchema):
    name: Annotated[str, Field(description="Nome do cliente", examples=["Yuri Cruz Torquato", ], max_length=30)]
    cpf: Annotated[
        str, Field(description="CPF do cliente", examples=["37422715553", ], pattern=r"^\d{11}$", min_length=11,
                   max_length=11)]
    age: Annotated[PositiveInt, Field(description="Idade do cliente", examples=[25, 67, 40, ], )]
    sex: Annotated[
        str, Field(description="Sexo do cliente (M ou F)", examples=["M", "F"], pattern="^[MF]$", min_length=1,
                   max_length=1)]
    address: Annotated[str, Field(description="Endereço do cliente", examples=["Rua Icapuí, 127", ], max_length=50)]


class ClientResponse(ClientRequest):
    id: Annotated[UUID, Field(description="Identificador do produto")]


class ClientUpdate(BaseSchema):
    age: Annotated[PositiveInt | None, Field(description="Idade do cliente", examples=[25, 67, 40, ], )] = None
    address: Annotated[str | None, Field(description="Endereço do cliente", examples=["Rua Icapuí, 127", ])] = None
