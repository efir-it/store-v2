from typing import Union

import uvicorn

from src.type_device.route import router as type_devise_router
from fastapi import FastAPI

app = FastAPI()
app.include_router(type_devise_router, prefix='/type_device')


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8080, reload=True, workers=3)
