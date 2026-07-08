from fastapi import FastAPI

from database import Base, engine
import models

from routers import auth, vendors, purchase_orders, reports

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Inventory Purchase & Vendor Management System"
)

app.include_router(auth.router)
app.include_router(vendors.router)
app.include_router(purchase_orders.router)
app.include_router(reports.router)


@app.get("/")
def home():
    return {
        "message": "Inventory Purchase & Vendor Management System API"
    }