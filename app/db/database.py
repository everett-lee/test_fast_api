from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from dynaconf import settings


SQLALCHEMY_DATABASE_URL = settings.DB_URL
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}, echo=True
# )
engine = create_engine(SQLALCHEMY_DATABASE_URL,
                    connect_args={'check_same_thread':False},
                    poolclass=StaticPool,
                    echo=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()