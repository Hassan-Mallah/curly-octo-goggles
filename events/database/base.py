import asyncio
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import async_scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_async_engine("postgresql+asyncpg://postgres:postgres@postgres/postgres")
db_session = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
session_factory = async_scoped_session(db_session, scopefunc=asyncio.current_task)

print(engine)
print(db_session)
print(session_factory)
Base = declarative_base()
