from typing import List, Optional
from pydantic import BaseModel


class DevicesBase(BaseModel):
    name: str
    hide: bool
    rmk_id: int
    type_device_id: int


class DevicesCreate(DevicesBase):
    pass


class DevicesUpdate(DevicesBase):
    pass


class Devices(DevicesBase):
    id: int

    class Config:
        orm_mode = True
