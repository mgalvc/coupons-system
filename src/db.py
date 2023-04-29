from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('postgresql://postgres:root@localhost:5432/spotlar', echo=True)
Session = sessionmaker(bind=engine)


def get_db():
    db = Session()
    yield db
    db.close()
    