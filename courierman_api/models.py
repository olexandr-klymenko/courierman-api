from datetime import time
from typing import List, Optional

from pydantic import BaseModel, Field
from pydantic import constr


class Address(BaseModel):
    city: str
    street: str
    building: str
    entrance: Optional[int]
    entrance_code: Optional[str]
    floor: Optional[int]
    flat: Optional[str]
    elevator: Optional[bool]


class CustomerInfo(BaseModel):
    address: Address
    name: str
    phone_number: str
    customer_class: str


class ProductItem(BaseModel):
    name: str
    price: float
    quantity: float
    total_price: float


class DeliverySlot(BaseModel):
    start_time: time
    finish_time: time


class Order(BaseModel):
    customer_info: CustomerInfo
    status: str
    delivery_slot: DeliverySlot
    boxes: List[str]
    virtual_boxes: List[str]
    weight: float
    payment_method: str
    payment_status: str
    actual_items_price: float
    comment: str
    items: List[ProductItem]


class Route(BaseModel):
    route_id: str
    store_info: str
    orders: List[Order]


Password = Field(min_length=6, max_length=14, regex="[a-zA-Z0-9,.;:\+\-_']")


class LoginRequest(BaseModel):
    phone_number: constr(max_length=50, strip_whitespace=True)
    password: str = Password


class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class PasswordChangeRequest(BaseModel):
    password: str = Password


class UserInfo(BaseModel):
    full_name: str
    phone_number: str
