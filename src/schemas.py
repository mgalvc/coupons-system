
from pydantic import BaseModel, validator
from datetime import datetime
from enum import Enum


class DiscountType(str, Enum):
    PERCENTAGE = 'PERCENTAGE'
    FIXED_FOR_ALL = 'FIXED_FOR_ALL'
    FIXED_FOR_FIRST_PURCHASE = 'FIXED_FOR_FIRST_PURCHASE'


class CouponBase(BaseModel):
    code: str
    expires_at: datetime
    max_usage: int
    min_purchase: float
    discount_type: DiscountType
    discount_value: float


class CreateCoupon(CouponBase):

    @validator('expires_at')
    def validate_date(cls, v):
        assert v > datetime.utcnow(), 'expiration date can\'t be in the past'
        return v


class Coupon(CouponBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class Purchase(BaseModel):
    amount: float
    is_first_purchase: bool


class Discount(BaseModel):
    coupon: str
    discount: float
