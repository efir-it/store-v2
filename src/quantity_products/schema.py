from pydantic import BaseModel


class QuantityProducts(BaseModel):
    count: int
    product: str
    store_id: int

    class Config:
        orm_mode = True
