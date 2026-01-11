import re
from datetime import datetime
from typing import Annotated
from uuid import UUID

from pydantic import EmailStr, Field, PositiveInt, AfterValidator

from app.schemas.base_schema import BaseSchema


def validade_cpf(v: str) -> str:
    """Valida CPF"""

    cpf = "".join(filter(str.isdigit, v))

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        raise ValueError("CPF inválido")

    for i in range(9, 11):
        total = sum(int(cpf[j]) * ((i + 1) - j) for j in range(i))
        digit = 0 if (total % 11) < 2 else 11 - (total % 11)

        if int(cpf[i]) != digit:
            raise ValueError("CPF inválido")

    return cpf


def validade_password(v: str) -> str:
    """Valida força da senha"""

    if len(v) < 8:
        raise ValueError("A senha deve ter, no mínimo, 8 caracteres")

    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&#])"
    if not re.match(pattern, v):
        raise ValueError(
            "A senha deve conter: maiúsculas, minúsculas, número e caractere especial"
        )

    return v


# Tipos customizados
CPF = Annotated[str, AfterValidator(validade_cpf)]
StrongPassword = Annotated[str, AfterValidator(validade_password)]


class ClientBase(BaseSchema):
    """Schema base com campos comuns"""

    name: Annotated[
        str,
        Field(
            description="Nome do cliente",
            examples=[
                "Yuri Cruz Torquato",
            ],
            max_length=30,
        ),
    ]
    cpf: Annotated[
        CPF,
        Field(
            description="CPF do cliente",
            examples=[
                "37422715553",
            ],
            pattern=r"^\d{11}$",
            min_length=11,
            max_length=11,
        ),
    ]
    email: Annotated[
        EmailStr,
        Field(
            description="Email do cliente",
            examples=[
                "iurikillzone@gmail.com",
            ],
            max_length=100,
        ),
    ]
    age: Annotated[
        PositiveInt,
        Field(
            description="Idade do cliente",
            examples=[
                25,
                67,
                40,
            ],
        ),
    ]
    sex: Annotated[
        str,
        Field(
            description="Sexo do cliente (M ou F)",
            examples=["M", "F"],
            pattern="^[MF]$",
            min_length=1,
            max_length=1,
        ),
    ]
    address: Annotated[
        str,
        Field(
            description="Endereço do cliente",
            examples=[
                "Rua Icapuí, 127",
            ],
            max_length=50,
        ),
    ]


class ClientRequest(ClientBase):
    """Schema para criação de client"""

    password: Annotated[
        StrongPassword,
        Field(
            description="Senha do cliente",
            examples=[
                "89755Yu@",
            ],
        ),
    ]


class ClientResponse(ClientBase):
    """Schema de resposta"""

    id: Annotated[UUID, Field(description="Identificador do cliente")]
    created_at: Annotated[datetime, Field(description="Data de criação do cliente")]
    updated_at: Annotated[datetime, Field(description="Data de atualização do cliente")]


class ClientUpdate(BaseSchema):
    email: Annotated[
        EmailStr | None,
        Field(
            description="Email do cliente",
            examples=[
                "iurikillzone@gmail.com",
            ],
            max_length=100,
        ),
    ] = None
    password: Annotated[
        StrongPassword | None,
        Field(
            description="Senha do cliente",
            examples=[
                "89755Yu@",
            ],
        ),
    ] = None
    age: Annotated[
        PositiveInt | None,
        Field(
            description="Idade do cliente",
            examples=[
                25,
                67,
                40,
            ],
        ),
    ] = None
    address: Annotated[
        str | None,
        Field(
            description="Endereço do cliente",
            examples=[
                "Rua Icapuí, 127",
            ],
        ),
    ] = None
