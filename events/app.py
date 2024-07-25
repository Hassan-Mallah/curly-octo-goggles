from fastapi import FastAPI
import uvicorn
from views import router_health
from views import router_events
from settings import settings

app = FastAPI()
app.include_router(router_health, prefix="/health", tags=["Health"])
app.include_router(router_events, prefix="/events", tags=["Events"])

if __name__ == "__main__":
    uvicorn.run("app:app", host='0.0.0.0', port=settings.EVENTS_PORT, reload=True)
