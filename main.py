from typing import Union

import uvicorn
from src.type_device import router as type_device
from src.devices import router as devices
from src.rmk import router as rmk
from fastapi import FastAPI

app = FastAPI()
app.include_router(type_device.router, prefix="/type_device", tags=["type_device"])
app.include_router(devices.router, prefix="/devices", tags=["devices"])
app.include_router(rmk.router, prefix="/rmk", tags=["rmk"])


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8080, reload=True, workers=3)
