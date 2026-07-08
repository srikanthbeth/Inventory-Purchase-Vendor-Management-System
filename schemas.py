from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import date


# ==========================
# User Schemas
# ==========================

class UserRegister(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    role: str

    class Config:
        from_attributes = True


# ==========================
# Vendor Schemas
# ==========================

class VendorCreate(BaseModel):
    vendor_name: str
    email: EmailStr
    phone: str
    address: str


class VendorUpdate(BaseModel):
    vendor_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    is_active: Optional[bool] = None


class VendorResponse(BaseModel):
    id: int
    vendor_name: str
    email: EmailStr
    phone: str
    address: str
    is_active: bool

    class Config:
        from_attributes = True


# ==========================
# Purchase Order Schemas
# ==========================

class PurchaseOrderCreate(BaseModel):
    vendor_id: int
    product_name: str

    quantity: int = Field(gt=0)
    unit_price: float = Field(gt=0)

    expected_delivery_date: date
    status: str = "Pending"


class PurchaseOrderUpdate(BaseModel):
    product_name: Optional[str] = None
    quantity: Optional[int] = Field(default=None, gt=0)
    unit_price: Optional[float] = Field(default=None, gt=0)
    expected_delivery_date: Optional[date] = None
    status: Optional[str] = None


class PurchaseOrderResponse(BaseModel):
    id: int
    vendor_id: int
    product_name: str
    quantity: int
    unit_price: float
    total_amount: float
    expected_delivery_date: date
    status: str

    class Config:
        from_attributes = True