from pydantic import BaseModel


class Drivers(BaseModel):
    name: str
    position_save: str
    model_device: str
