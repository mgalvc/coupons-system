class BaseCouponException(Exception):

	def __init__(self, code, description):
		self.__code = code
		self.__description = description
	
	@property
	def description(self):
		return self.__description

	@property
	def http_status_code(self):
		return self.__code


class DuplicatedCouponCode(BaseCouponException):
	
	def __init__(self):
		super().__init__(409, 'There already is a coupon with this code')


class CouponNotFound(Exception):
	
	def __init__(self):
		super().__init__(404, 'Coupon not found')


class CouponExceededMaxUsage(Exception):
	
	def __init__(self):
		super().__init__(400, 'Coupon exceeded maximum usage')


class CouponExpired(Exception):
	
	def __init__(self):
		super().__init__(400, 'Coupon expired')


class PurchaseAmountNotReached(Exception):
	
	def __init__(self):
		super().__init__(400, 'Minimun purchase amount not reached')


class NotFirstPurchase(Exception):
	
	def __init__(self):
		super().__init__(400, 'Coupon for first purchase only')