from fastapi import FastAPI, Depends, HTTPException
from .exceptions import BaseCouponException
from .schemas import CreateCoupon, Coupon, Discount, Purchase
from .db import get_db
from .repository import CouponRepo
from .usecases import CouponUsecases


app = FastAPI()


@app.post('/api/coupons', response_model=Coupon, status_code=201)
async def create(coupon: CreateCoupon, session = Depends(get_db)):
	usecases = CouponUsecases(CouponRepo(session))
	
	try:
		return await usecases.create_coupon(coupon)
	except BaseCouponException as exc:
		raise HTTPException(status_code=exc.http_status_code, detail=exc.description)


@app.post('/api/coupons/{code}/burn', response_model=Discount, status_code=200)
async def burn(code: str, purchase: Purchase, session = Depends(get_db)):
	usecases = CouponUsecases(CouponRepo(session))

	try:
		return await usecases.burn_coupon(code, purchase)
	except BaseCouponException as exc:
		raise HTTPException(status_code=exc.http_status_code, detail=exc.description)
