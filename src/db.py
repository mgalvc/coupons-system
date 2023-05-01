from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
from .config import settings


url = URL.create(
    drivername='postgresql',
    username=settings.DB_USERNAME,
    password=settings.DB_PASSWORD,
    host=settings.DB_HOST,
    database=settings.DB_NAME
)
engine = create_engine(url, echo=True)
Session = sessionmaker(bind=engine)


def get_db():
    db = Session()
    yield db
    db.close()
