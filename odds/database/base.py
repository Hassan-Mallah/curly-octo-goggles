import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import async_scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import select

__all__ = ["Base", "get_session", "get_row", "get_rows"]

engine = create_async_engine("postgresql+asyncpg://postgres:postgres@postgres/postgres")
db_session = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
session_factory = async_scoped_session(db_session, scopefunc=asyncio.current_task)

Base = declarative_base()


async def get_session():
    async with db_session() as session:
        yield session


async def get_row(session, model, row_id: str, update: bool = False):
    """get row from db in case of update lock the row"""

    query = select(model).where(model.id == row_id)
    if update:
        query = query.with_for_update()

    result = await session.execute(query)
    row = result.scalars().first()

    return row


async def get_rows(session, model, event_id):
    result = await session.execute(select(model).where(model.event_id == event_id))
    row = result.scalars().all()

    return row
