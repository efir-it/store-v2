from typing import Optional
from pydantic import BaseModel


class TypeDeviceBase(BaseModel):
    name: str


class TypeDeviceCreate(TypeDeviceBase):
    name: str


class TypeDeviceUpdate(TypeDeviceBase):
    ...


class TypeDevice(TypeDeviceBase):
    id: int

    class Config:
        orm_mode = True
