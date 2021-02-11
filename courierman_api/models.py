from datetime import time
from typing import List, Optional

from pydantic import BaseModel, Field, HttpUrl


class AddressBrief(BaseModel):
    street: str = Field(..., title="Localized street name")
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
    customer_type: str


class ProductItem(BaseModel):
    name: str = Field(..., title="Localized product name")
    price: float = Field(..., title="Price per unit")
    amount: float
    unit: str = Field(..., title="Localized amount unit")
    bundle: int = Field(..., title="Amount in bundle. Unused")
    weight: float
    total_price: float = Field(..., title="Total price")
    image: HttpUrl


class DeliverySlot(BaseModel):
    start_time: time
    finish_time: time


class OrderStatus(BaseModel):
    status_enum: str = Field(
        ...,
        title="Order status enum",
        description="""
    'delivered': заказ который отмечен курьером как доставлен (кнопка внутри заказа)
    'delivering': заказ который у курьера на борту
    'assembled': заказ который еще у кладовщика и ожидает отгрузки курьеру
    'assembling': заказ который еще собирается сборщиком
    'canceled': заказ который по тем или иным причинам был отменен
    """,
    )
    status_name: str = Field(..., title="Localized order status")


class PaymentMethod(BaseModel):
    method_enum: str = Field(
        ...,
        title="Payment method enum",
        description="""
    'cash': Наличные
    'on_site': На сайте
    'terminal': Терминал
    'cashless': Б/Н""",
    )
    method_name: str = Field(..., title="Localized payment method")


class PaymentStatus(BaseModel):
    status_enum: str = Field(
        ...,
        title="Payment status enum",
        description="""
    'paid': Заказ оплачн
    'not_paid': Заказ не оплачен
    """,
    )
    status_name: str = Field(..., title="Localized payment status")


class OrderBrief(BaseModel):
    order_secret: str
    status: OrderStatus
    address: AddressBrief
    delivery_slot: DeliverySlot
    boxes: List[str]
    virtual_boxes: List[str]
    weight: float
    weight_unit: str = Field(..., title="Localized weight unit")
    payment_method: PaymentMethod
    payment_status: PaymentStatus
    actual_items_price: float
    currency: str = Field(..., title="Localized currency unit")
    comment: str


class OrderFull(OrderBrief):
    customer_info: CustomerInfo
    items: List[ProductItem]


class StoreInfo(BaseModel):
    chain_logo: HttpUrl
    address: AddressBrief


class RouteBrief(BaseModel):
    route_id: str
    start_point: StoreInfo
    delivery_slot: DeliverySlot
    is_loaded: bool
    is_completed: bool
    number_of_orders: int


class RouteFull(RouteBrief):
    orders: List[OrderBrief]


Password = Field(min_length=6, max_length=14, regex="[a-zA-Z0-9,.;:\+\-_']")


class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class PasswordChangeRequest(BaseModel):
    current_password: str
    new_password: str = Password


class UserInfo(BaseModel):
    full_name: str
    phone_number: str
