import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import async_scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import select

engine = create_async_engine("postgresql+asyncpg://postgres:postgres@postgres/postgres")
db_session = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
session_factory = async_scoped_session(db_session, scopefunc=asyncio.current_task)

Base = declarative_base()


async def get_session():
    async with db_session() as session:
        yield session


async def get_row(session, model, event_id):
    result = await session.execute(select(model).where(model.id == event_id))
    row = result.scalars().first()

    return row
