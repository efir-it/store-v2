from pydantic import BaseModel


class Store(BaseModel):
    name = str
    address = str
    separated = int
    hide = bool = True

