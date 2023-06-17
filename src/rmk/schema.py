from typing import List

from pydantic import BaseModel


class RmkBase(BaseModel):
    name: str


class RmkCreate(RmkBase):
    pass


class RmkUpdate(RmkBase):
    pass


class Rmk(RmkBase):
    id: int

    class Config:
        orm_mode = True