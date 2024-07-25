from fastapi import FastAPI
import uvicorn
from sqlalchemy import select
from database.base import db_session
from sqlalchemy import text
from views import router_health
from views import router_odds

app = FastAPI()
app.include_router(router_health, prefix="/health", tags=["Health"])
app.include_router(router_odds, prefix="/events", tags=["Odds"])

@app.get("/")
async def read_root():
    async with db_session() as session:
        print(session)
        result = await session.execute(select(1))
        print(result.scalar())

        result = await session.execute(text("select * from odds"))
        for row in result:
            print(row)

        print('done')

    return {"Hello": "Odds"}


if __name__ == "__main__":
    uvicorn.run("app:app", host='0.0.0.0', port=5050, reload=True, workers=3)
