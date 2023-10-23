from sqlalchemy import BigInteger
from sqlalchemy.orm import relationship, Mapped, mapped_column, DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from config import SQLALCHEMY_URL


engine = create_async_engine(SQLALCHEMY_URL, echo=True)
