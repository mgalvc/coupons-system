from .schemas import CreateCoupon, Purchase, DiscountType, Discount
from .repository import CouponRepo
from datetime import datetime
from . import exceptions


class CouponUsecases:
    
	def __init__(self, repo: CouponRepo):
		self.__repo = repo

	async def create_coupon(self, coupon: CreateCoupon):
		return await self.__repo.create(coupon)

	async def burn_coupon(self, code: str, purchase: Purchase):
		coupon = await self.__repo.get_by_code(code)
		
		if len(coupon.burned) == coupon.max_usage:
			raise exceptions.CouponExceededMaxUsage
		if datetime.utcnow() > coupon.expires_at:
			raise exceptions.CouponExpired
		if purchase.purchase_value < coupon.min_purchase:
			raise exceptions.PurchaseAmountNotReached
		if coupon.discount_type == DiscountType.FIXED_FOR_FIRST_PURCHASE and not purchase.is_first_purchase:
			raise exceptions.NotFirstPurchase

		discount_value = coupon.discount_value

		if coupon.discount_type == DiscountType.PERCENTAGE:
			discount_value = purchase.purchase_value * coupon.discount_value

		await self.__repo.burn(coupon)

		return Discount(coupon=code, discount=discount_value)