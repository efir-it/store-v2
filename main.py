from fastapi import FastAPI
import uvicorn
from src.quantity_products import router as quantity_products
from src.store import router as store


app = FastAPI()

app.include_router(quantity_products.router, prefix="/quantity_products", tags=["Остатки товаров"])
app.include_router(store.router, prefix="/store", tags=["Торговая точка"])

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8080, reload=True, workers=3)
