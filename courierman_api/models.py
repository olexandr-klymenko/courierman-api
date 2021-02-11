from datetime import time
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class AddressBrief(BaseModel):
    street: str = Field(default_factory=str, title="Localized street name")
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
    name: str = Field(default_factory=str, title="Localized product name")
    price: float = Field(default_factory=float, title="Price per unit")
    amount: float
    unit: str = Field(default_factory=str, title="Localized amount unit")
    bundle: int = Field(default_factory=int, title="Amount in bundle. Unused")
    weight: float
    total_price: float = Field(default_factory=float, title="Total price")
    image: str = Field(default_factory=str, title="URL of product image")


class DeliverySlot(BaseModel):
    start_time: time
    finish_time: time


class OrderStatusEnum(Enum):
    """
    'delivered': заказ который отмечен курьером как доставлен (кнопка внутри заказа)<br>
    'delivering': заказ который у курьера на борту<br>
    'assembled': заказ который еще у кладовщика и ожидает отгрузки курьеру<br>
    'assembling': заказ который еще собирается сборщиком<br>
    'canceled': заказ который по тем или иным причинам был отменен
    """

    delivered = "delivered"
    delivering = "delivering"
    assembled = "assembled"
    assembling = "assembling"
    canceled = "canceled"


class OrderStatus(BaseModel):
    status: OrderStatusEnum
    status_name: str = Field(default_factory=str, title="Localized order status")


class PaymentMethodEnum(Enum):
    """
    'cash': Наличные<br>
    'on_site': На сайте<br>
    'terminal': Терминал<br>
    'cashless': Б/Н
    """

    cash = "cash"
    on_site = "on_site"
    terminal = "terminal"
    cashless = "cashless"


class PaymentMethod(BaseModel):
    method: PaymentMethodEnum
    method_name: str = Field(default_factory=str, title="Localized payment method")


class PaymentStatusEnum(Enum):
    """
    'paid': Заказ оплачн<br>
    'not_paid': Заказ не оплачен
    """

    paid = "paid"
    not_paid = "not_paid"


class PaymentStatus(BaseModel):
    status: PaymentStatusEnum
    status_name: str = Field(default_factory=str, title="Localized payment status")


class OrderBrief(BaseModel):
    order_secret: str
    status: OrderStatus
    address: AddressBrief
    delivery_slot: DeliverySlot
    boxes: List[str]
    virtual_boxes: List[str]
    weight: float
    weight_unit: str = Field(default_factory=str, title="Localized weight unit")
    payment_method: PaymentMethod
    payment_status: PaymentStatus
    actual_items_price: float
    currency: str = Field(default_factory=str, title="Localized currency unit")
    comment: str


class OrderFull(OrderBrief):
    customer_info: CustomerInfo
    items: List[ProductItem]


class StoreInfo(BaseModel):
    chain_logo: str = Field(default_factory=str, title="URL of chain logo image")
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
