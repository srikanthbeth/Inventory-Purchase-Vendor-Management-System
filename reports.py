from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from database import get_db
from models import PurchaseOrder
from dependencies import admin_or_store_manager

router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)


# ==========================================
# Purchase History by Vendor
# ==========================================
@router.get("/vendor/{vendor_id}")
def purchase_history(
    vendor_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(admin_or_store_manager)
):

    orders = db.query(PurchaseOrder).filter(
        PurchaseOrder.vendor_id == vendor_id
    ).all()

    return orders


# ==========================================
# Filter Orders by Status
# ==========================================
@router.get("/status/{status}")
def filter_status(
    status: str,
    db: Session = Depends(get_db),
    current_user=Depends(admin_or_store_manager)
):

    orders = db.query(PurchaseOrder).filter(
        PurchaseOrder.status == status
    ).all()

    return orders


# ==========================================
# Search Orders by Product Name
# ==========================================
@router.get("/search/")
def search_product(
    product_name: str,
    db: Session = Depends(get_db),
    current_user=Depends(admin_or_store_manager)
):

    orders = db.query(PurchaseOrder).filter(
        PurchaseOrder.product_name.ilike(f"%{product_name}%")
    ).all()

    return orders


# ==========================================
# Pagination
# ==========================================
@router.get("/pagination/")
def pagination(
    page: int = Query(1, ge=1),
    limit: int = Query(5, ge=1),
    db: Session = Depends(get_db),
    current_user=Depends(admin_or_store_manager)
):

    skip = (page - 1) * limit

    orders = db.query(PurchaseOrder).offset(skip).limit(limit).all()

    return {
        "page": page,
        "limit": limit,
        "data": orders
    }