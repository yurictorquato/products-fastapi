"""Exceções customizadas da aplicação."""

from uuid import UUID


class ProductNotFoundException(Exception):
    """Exceção lançada quando um produto não é encontrado."""

    def __init__(self, product_id: UUID) -> None:
        self.product_id: UUID = product_id
        self.message = f"Produto com ID {product_id} não foi encontrado."
        super().__init__(self.message)


class InvalidProductDataException(Exception):
    """Exceção lançada quando os dados do produto são inválidos."""

    def __init__(self, message: str) -> None:
        self.message: str = message
        super().__init__(self.message)
