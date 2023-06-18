from pydantic import BaseModel


class Store(BaseModel):
    name = str
    address = str
    separated = bool
    rmk_id: int

