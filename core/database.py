# from typing import AsyncGenerator
# from sqlalchemy import MetaData
# from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
#
# from config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER
#
# DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# Base = declarative_base()
# metadata = MetaData()
#
# engine = create_async_engine(DATABASE_URL)
# async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
#
#
# async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
#     async with async_session_maker() as session:
#         yield session


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:542525Zz@localhost:5432/store"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, extend_existing=True)
Base: DeclarativeMeta = declarative_base()


def get_db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
