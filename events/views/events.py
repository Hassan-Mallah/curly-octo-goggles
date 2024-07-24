from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import Response
from sqlalchemy import select

from .dto import EventDto
from database.models import Event
from database.base import db_session

__all__ = ["router"]

router = APIRouter()


@router.get("/{event_id}", name="get event", response_description="Get event by id")
async def get_health_check(event_id: str) -> dict:
    async with db_session() as session:
        result = await session.execute(select(Event).where(Event.id == event_id))
        event = result.scalars().first()

        if event:
            print(Event.to_dict(event))
            return Event.to_dict(event)
        else:
            return {'message': 'Event not found'}

@router.get("/", name="get events", response_description="Get all events")
async def get_health_check() -> list:
    async with db_session() as session:
        result = await session.execute(select(Event))
        events = result.scalars().all()
        print(events)
        # for event in events:
        #     print(event.to_dict
        # return []
        return [event.to_dict() for event in events]
        if event:
            print(Event.to_dict(event))
            return Event.to_dict(event)
        else:
            return {'message': 'Event not found'}
    return []


@router.post("/", name="create event", response_description="Create a new event")
async def create_event(_: Request, data: EventDto) -> Response:
    async with db_session() as session:
        event = Event(
            id=data.id,
            name=data.name,
            location=data.location,
            teams=data.teams,
        )
        session.add(event)
        await session.commit()


    return []
