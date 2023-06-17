from pydantic import BaseModel


class Store(BaseModel):
    name = str
    address = str
    separated = bool
    hide = bool = True

