from fastapi import FastAPI
import uvicorn
import asyncio
# import psycopg2
from sqlalchemy import select
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import async_scoped_session

app = FastAPI()

engine = create_async_engine("postgresql+asyncpg://postgres:postgres@postgres:5432/postgres")
db_session = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
session_factory = async_scoped_session(db_session, scopefunc=asyncio.current_task)

print(engine)
print(db_session)
print(session_factory)


@app.get("/")
async def read_root():
    async with db_session() as session:
        print(session)
        result = await session.execute(select(1))
        print(result.scalar())

        print('done')

    return {"Hello": "Odds"}


if __name__ == "__main__":
    uvicorn.run("app:app", host='0.0.0.0', port=5050, reload=True, workers=3)
