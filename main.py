import uvicorn
from src.type_device import router as type_device
from src.devices import router as devices
from src.rmk import router as rmk
from src.quantity_products import router as quantity_products

from src.drivers import router as drivers
from src.store import router as store
from fastapi import FastAPI

app = FastAPI()
app.include_router(type_device.router, prefix="/type_device", tags=["type_device"])
app.include_router(devices.router, prefix="/devices", tags=["devices"])
app.include_router(rmk.router, prefix="/rmk", tags=["rmk"])
app.include_router(quantity_products.router, prefix="/quantity_products", tags=["quantity_products"])


app.include_router(drivers.router, prefix="/drivers", tags=["drivers"])
app.include_router(store.router, prefix="/store", tags=["store"])

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8080, reload=True, workers=3)
