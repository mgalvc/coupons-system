import pytest
from src.repository import CouponRepo
from src.usecases import CouponUsecases
from src.schemas import CreateCoupon, DiscountType, Purchase
from datetime import datetime, timedelta
from src.models import Base
from uuid import uuid4


@pytest.fixture(scope="function")
def sqlalchemy_declarative_base():
    return Base


@pytest.fixture(scope="function")
def sqlalchemy_mock_config():
	return [
		('coupon', [
			{
				'id': 1,
				'code': '123',
				'expires_at': datetime.utcnow() + timedelta(days=1),
				'max_usage': 1,
				'min_purchase': 100,
				'discount_type': DiscountType.PERCENTAGE,
				'discount_value': 0.1
			},
			{
				'id': 2,
				'code': 'coupon_with_max_usage',
				'expires_at': datetime.utcnow() + timedelta(days=1),
				'max_usage': 1,
				'min_purchase': 100,
				'discount_type': DiscountType.FIXED_FOR_ALL,
				'discount_value': 10
			},
			{
				'id': 3,
				'code': 'coupon_expired',
				'expires_at': datetime.utcnow() - timedelta(days=1),
				'max_usage': 1,
				'min_purchase': 100,
				'discount_type': DiscountType.FIXED_FOR_ALL,
				'discount_value': 10
			},
			{
				'id': 4,
				'code': 'high_purchase_amount',
				'expires_at': datetime.utcnow() + timedelta(days=1),
				'max_usage': 1,
				'min_purchase': 500,
				'discount_type': DiscountType.FIXED_FOR_ALL,
				'discount_value': 10
			},
			{
				'id': 5,
				'code': 'for_first_purchase',
				'expires_at': datetime.utcnow() + timedelta(days=1),
				'max_usage': 1,
				'min_purchase': 100,
				'discount_type': DiscountType.FIXED_FOR_FIRST_PURCHASE,
				'discount_value': 10
			}
		]),
		('burned_coupon', [
			{
				'id': 1,
				'coupon_id': 2
			}
		])
	]


@pytest.fixture
def coupon_repo(mocked_session):
	return CouponRepo(mocked_session)


@pytest.fixture
def coupon_schema():
	return CreateCoupon(
        code=str(uuid4()),
        expires_at=datetime.utcnow() + timedelta(days=1),
        max_usage=1,
        min_purchase=100,
        discount_type=DiscountType.FIXED_FOR_ALL,
        discount_value=5
	)


@pytest.fixture
def purchase_schema():
	return Purchase(amount=100, is_first_purchase=False)


@pytest.fixture
def coupon_usecases(coupon_repo):
	return CouponUsecases(coupon_repo)