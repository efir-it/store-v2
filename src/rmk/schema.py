from pydantic import BaseModel


class Rmk(BaseModel):
    name: str

    class Config:
        orm_mode = True
