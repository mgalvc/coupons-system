from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from datetime import datetime


class Base(DeclarativeBase):
    ...


class Coupon(Base):
	__tablename__ = 'coupon'

	id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
	code: Mapped[str] = mapped_column(unique=True)
	expires_at: Mapped[datetime]
	max_usage: Mapped[int]
	min_purchase: Mapped[float]
	discount_type: Mapped[str]
	discount_value: Mapped[float]
	created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow())
    
	burned: Mapped[list['BurnedCoupon']] = relationship(back_populates='coupon')


class BurnedCoupon(Base):
	__tablename__ = 'burned_coupon'

	id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
	coupon_id: Mapped[int] = mapped_column(ForeignKey('coupon.id'))
	created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow())
    
	coupon: Mapped['Coupon'] = relationship(back_populates='burned')