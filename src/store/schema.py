from pydantic import BaseModel


class Store(BaseModel):
    name: str
    address: str
    separated: bool

    class Config:
        orm_mode = True

