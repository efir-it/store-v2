from pydantic import BaseModel


class QuantityProducts(BaseModel):
    count: int
