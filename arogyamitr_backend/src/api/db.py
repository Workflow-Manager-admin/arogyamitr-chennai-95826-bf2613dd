"""
Database setup with SQLAlchemy ORM for SQLite, plus a sample User model and initialization.

This module configures the SQLAlchemy engine to use SQLite as the backend
and provides a simple User model and helper to create all tables.
"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# For SQLite database: file based (default: arogya.sqlite in backend root)
SQLALCHEMY_DATABASE_URL = "sqlite:///./arogya.sqlite"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# PUBLIC_INTERFACE
class User(Base):
    """
    Example User table for FastAPI-SQLAlchemy integration.
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)


# PUBLIC_INTERFACE
def init_db():
    """
    Creates all tables in the SQLite DB using SQLAlchemy models.
    Typically called at app startup.
    """
    Base.metadata.create_all(bind=engine)
