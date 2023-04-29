from sqlalchemy.orm import Session
from .schemas import CreateCoupon
from .models import Coupon, BurnedCoupon
from sqlalchemy.exc import IntegrityError
from .exceptions import DuplicatedCouponCode, CouponNotFound

class CouponRepo:

	def __init__(self, session: Session):
		self.__session = session

	async def create(self, coupon_schema: CreateCoupon):
		try:
			coupon = Coupon(
				code=coupon_schema.code,
				expires_at=coupon_schema.expires_at,
				max_usage=coupon_schema.max_usage,
				min_purchase=coupon_schema.min_purchase,
				discount_type=coupon_schema.discount_type,
				discount_value=coupon_schema.discount_value
			)
			self.__session.add(coupon)
			self.__session.commit()
			self.__session.refresh(coupon)
			return coupon
		except IntegrityError:
			raise DuplicatedCouponCode
		
	async def get_by_code(self, code: str):
		coupon = self.__session.query(Coupon).filter(Coupon.code == code).first()
		if not coupon:
			raise CouponNotFound
		return coupon
	
	async def burn(self, coupon: Coupon):
		coupon.burned.append(BurnedCoupon())
		self.__session.commit()