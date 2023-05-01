import pytest
from src.models import Coupon, BurnedCoupon
from src import exceptions as exc
from src.schemas import Discount


@pytest.mark.asyncio
async def test_create_coupon_success(coupon_schema, coupon_usecases):
	coupon = await coupon_usecases.create_coupon(coupon_schema)
	assert isinstance(coupon, Coupon)
    

@pytest.mark.asyncio
async def test_create_coupon_duplicated(coupon_schema, coupon_usecases):
	coupon_schema.code = '123'
	with pytest.raises(exc.DuplicatedCouponCode):
		await coupon_usecases.create_coupon(coupon_schema)

    
@pytest.mark.asyncio
async def test_burn_coupon_success(coupon_usecases, purchase_schema):
	discount = await coupon_usecases.burn_coupon('123', purchase_schema)
	assert discount == Discount(coupon='123', discount=10)
    
	with pytest.raises(exc.CouponExceededMaxUsage):
		await coupon_usecases.burn_coupon('123', purchase_schema)


@pytest.mark.asyncio
async def test_burn_coupon_exceptions(mocked_session, purchase_schema, coupon_usecases):
	with pytest.raises(exc.CouponExceededMaxUsage):
		await coupon_usecases.burn_coupon('coupon_with_max_usage', purchase_schema)

	with pytest.raises(exc.CouponExpired):
		await coupon_usecases.burn_coupon('coupon_expired', purchase_schema)

	with pytest.raises(exc.PurchaseAmountNotReached):
		await coupon_usecases.burn_coupon('high_purchase_amount', purchase_schema)

	with pytest.raises(exc.NotFirstPurchase):
		await coupon_usecases.burn_coupon('for_first_purchase', purchase_schema)

	with pytest.raises(exc.CouponNotFound):
		await coupon_usecases.burn_coupon('fake', purchase_schema)

