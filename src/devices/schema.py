from pydantic import BaseModel


class Devices(BaseModel):
    name: str
    hide: bool
