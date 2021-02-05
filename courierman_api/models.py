from datetime import time
from typing import List, Optional

from pydantic import BaseModel, Field
from pydantic import constr


class AddressBrief(BaseModel):
    street: str
    building: str


class AddressFull(AddressBrief):
    city: str
    block: Optional[int]
    entrance: Optional[int]
    entrance_code: Optional[str]
    floor: Optional[int]
    flat: Optional[str]
    office: Optional[str]
    company: Optional[str]
    is_elevator: Optional[bool]


class CustomerInfo(BaseModel):
    address: AddressFull
    name: str
    phone_number: str
    customer_type: str


class ProductItem(BaseModel):
    name: str
    price: float
    quantity: float
    weight: float
    total_price: float
    image: str


class DeliverySlot(BaseModel):
    start_time: time
    finish_time: time


class OrderBrief(BaseModel):
    status: str
    address: AddressBrief
    delivery_slot: DeliverySlot
    boxes: List[str]
    virtual_boxes: List[str]
    weight: float
    payment_method: str
    payment_status: str
    actual_items_price: float
    comment: str


class OrderFull(OrderBrief):
    customer_info: CustomerInfo
    items: List[ProductItem]


class StoreInfo(BaseModel):
    chain_logo: str
    address: AddressBrief


class RouteBrief(BaseModel):
    route_id: str
    start_point: AddressBrief
    delivery_slot: DeliverySlot
    is_completed: bool
    number_of_orders: int


class RouteFull(BaseModel):
    route_id: str
    store_info: StoreInfo
    is_completed: bool
    orders: List[OrderBrief]


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
