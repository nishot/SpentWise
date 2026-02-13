from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import setting

SQL_CONNECTION_STRING = (
    f"postgresql://{setting.database_username}:{setting.database_password}"
    f"@{setting.database_hostname}:{setting.database_port}/{setting.database_name}"
)

engine = create_engine(SQL_CONNECTION_STRING, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
