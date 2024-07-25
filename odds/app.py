from fastapi import FastAPI
import uvicorn
from views import router_health
from views import router_odds
from settings import settings

app = FastAPI()
app.include_router(router_health, prefix="/health", tags=["Health"])
app.include_router(router_odds, prefix="/events", tags=["Odds"])

if __name__ == "__main__":
    uvicorn.run("app:app", host='0.0.0.0', port=settings.ODDS_PORT, reload=True)
