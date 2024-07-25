from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import select
from settings import settings

__all__ = ["Base", "get_session", "get_row"]

engine = create_async_engine(settings.DB_URL)
db_session = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
Base = declarative_base()


async def get_session():
    async with db_session() as session:
        yield session


async def get_row(session, model, event_id: str, update: bool = False):
    """get row from db, in case of update lock the row"""

    query = select(model).where(model.id == event_id)
    if update:
        query = query.with_for_update()

    result = await session.execute(query)
    row = result.scalars().first()

    return row
