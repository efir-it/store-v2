from pydantic import BaseModel


class QuantityProducts(BaseModel):
    count: int
    product_id: int
    store_id: int

