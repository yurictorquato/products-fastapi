from pydantic import BaseModel


class BaseSchema(BaseModel):
    model_config = {
        "extra": "forbid",
        "from_attributes": True,
        "arbitrary_types_allowed": True,
    }
