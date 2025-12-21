from typing import Annotated

from pydantic import Field, PositiveFloat, PositiveInt, UUID4

from app.schemas.base_schema import BaseSchema


class ProductRequest(BaseSchema):
    name: Annotated[
        str,
        Field(
            description="Nome do produto",
            examples=[
                "Iphone",
                "Ipad",
            ],
            max_length=25,
        ),
    ]
    price: Annotated[
        PositiveFloat,
        Field(
            description="Preço do produto",
            examples=[
                77.5,
                1_000.75,
            ],
        ),
    ]
    quantity: Annotated[
        PositiveInt,
        Field(
            description="Quantidade do produto",
            examples=[
                6,
                10,
                0,
            ],
        ),
    ]


class ProductResponse(ProductRequest):
    id: Annotated[UUID4, Field(description="Identificador do produto")]


class ProductUpdate(BaseSchema):
    price: Annotated[
        PositiveFloat | None,
        Field(
            description="Preço do produto",
            examples=[
                77.5,
                1_000.75,
            ],
        ),
    ] = None
    quantity: Annotated[
        PositiveInt | None,
        Field(
            description="Quantidade do produto",
            examples=[
                6,
                10,
                0,
            ],
        ),
    ] = None
