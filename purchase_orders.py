from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import Vendor, PurchaseOrder
from schemas import PurchaseOrderCreate, PurchaseOrderUpdate
from dependencies import admin_or_store_manager

router = APIRouter(
    prefix="/purchase-orders",
    tags=["Purchase Order Management"]
)


# ==================================
# Create Purchase Order
# ==================================
@router.post("/")
def create_purchase_order(
    order: PurchaseOrderCreate,
    db: Session = Depends(get_db),
    current_user=Depends(admin_or_store_manager)
):

    vendor = db.query(Vendor).filter(
        Vendor.id == order.vendor_id
    ).first()

    if not vendor:
        raise HTTPException(
            status_code=404,
            detail="Vendor not found"
        )

    if not vendor.is_active:
        raise HTTPException(
            status_code=400,
            detail="Purchase order cannot be created for an inactive vendor."
        )

    total_amount = order.quantity * order.unit_price

    new_order = PurchaseOrder(
        vendor_id=order.vendor_id,
        product_name=order.product_name,
        quantity=order.quantity,
        unit_price=order.unit_price,
        total_amount=total_amount,
        expected_delivery_date=order.expected_delivery_date,
        status=order.status
    )

    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    return {
        "message": "Purchase Order Created Successfully",
        "purchase_order": new_order
    }


# ==================================
# Get All Purchase Orders
# ==================================
@router.get("/")
def get_all_orders(
    db: Session = Depends(get_db),
    current_user=Depends(admin_or_store_manager)
):

    orders = db.query(PurchaseOrder).all()

    return orders


# ==================================
# Get Purchase Order By ID
# ==================================
@router.get("/{order_id}")
def get_order(
    order_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(admin_or_store_manager)
):

    order = db.query(PurchaseOrder).filter(
        PurchaseOrder.id == order_id
    ).first()

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Purchase Order not found"
        )

    return order


# ==================================
# Update Purchase Order
# ==================================
@router.put("/{order_id}")
def update_order(
    order_id: int,
    order: PurchaseOrderUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(admin_or_store_manager)
):

    db_order = db.query(PurchaseOrder).filter(
        PurchaseOrder.id == order_id
    ).first()

    if not db_order:
        raise HTTPException(
            status_code=404,
            detail="Purchase Order not found"
        )

    if db_order.status == "Received":
        raise HTTPException(
            status_code=400,
            detail="Received orders cannot be edited."
        )

    update_data = order.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_order, key, value)

    db_order.total_amount = (
        db_order.quantity * db_order.unit_price
    )

    db.commit()
    db.refresh(db_order)

    return {
        "message": "Purchase Order Updated Successfully",
        "purchase_order": db_order
    }