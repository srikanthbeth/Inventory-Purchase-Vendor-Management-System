from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import Vendor
from schemas import VendorCreate, VendorUpdate
from dependencies import admin_only

router = APIRouter(
    prefix="/vendors",
    tags=["Vendor Management"]
)


# ===========================
# Create Vendor
# ===========================
@router.post("/")
def create_vendor(
    vendor: VendorCreate,
    db: Session = Depends(get_db),
    current_user=Depends(admin_only)
):

    existing_vendor = db.query(Vendor).filter(
        Vendor.email == vendor.email
    ).first()

    if existing_vendor:
        raise HTTPException(
            status_code=400,
            detail="Vendor email already exists"
        )

    new_vendor = Vendor(
        vendor_name=vendor.vendor_name,
        email=vendor.email,
        phone=vendor.phone,
        address=vendor.address
    )

    db.add(new_vendor)
    db.commit()
    db.refresh(new_vendor)

    return {
        "message": "Vendor Created Successfully",
        "vendor": new_vendor
    }


# ===========================
# Get All Vendors
# ===========================
@router.get("/")
def get_all_vendors(
    db: Session = Depends(get_db),
    current_user=Depends(admin_only)
):

    vendors = db.query(Vendor).all()

    return vendors


# ===========================
# Get Vendor By ID
# ===========================
@router.get("/{vendor_id}")
def get_vendor(
    vendor_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(admin_only)
):

    vendor = db.query(Vendor).filter(
        Vendor.id == vendor_id
    ).first()

    if not vendor:
        raise HTTPException(
            status_code=404,
            detail="Vendor not found"
        )

    return vendor


# ===========================
# Update Vendor
# ===========================
@router.put("/{vendor_id}")
def update_vendor(
    vendor_id: int,
    vendor: VendorUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(admin_only)
):

    db_vendor = db.query(Vendor).filter(
        Vendor.id == vendor_id
    ).first()

    if not db_vendor:
        raise HTTPException(
            status_code=404,
            detail="Vendor not found"
        )

    update_data = vendor.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_vendor, key, value)

    db.commit()
    db.refresh(db_vendor)

    return {
        "message": "Vendor Updated Successfully",
        "vendor": db_vendor
    }


# ===========================
# Soft Delete Vendor
# ===========================
@router.delete("/{vendor_id}")
def delete_vendor(
    vendor_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(admin_only)
):

    vendor = db.query(Vendor).filter(
        Vendor.id == vendor_id
    ).first()

    if not vendor:
        raise HTTPException(
            status_code=404,
            detail="Vendor not found"
        )

    vendor.is_active = False

    db.commit()

    return {
        "message": "Vendor Deactivated Successfully"
    }