import settings
from loguru import logger
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from contextlib import contextmanager


engine = create_engine(settings.SQLALCHEMY_DATABASE_URL, echo=False)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()


@contextmanager
def get_db():
    db = SessionLocal()
    logger.info("DB session created")
    try:
        yield db
    finally:
        logger.info("Closing DB session")
        db.close()
