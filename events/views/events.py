from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from starlette.requests import Request
from sqlalchemy import select
from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession

from .dto import EventDto
from .dto import EventDetailDto
from database.models import Event
from database.base import get_session
from database.base import get_row

__all__ = ["router"]

router = APIRouter()


@router.get("/{event_id}", name="get event", response_description="Get event by id")
async def get_event_by_id(_: Request, event_id: str, session: AsyncSession = Depends(get_session)) -> dict:
    event = await get_row(session, Event, event_id)
    if event:
        return Event.to_dict(event)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event not found")


@router.get("/", name="get events", response_description="Get all events")
async def get_events(_: Request, session: AsyncSession = Depends(get_session)) -> list:
    result = await session.execute(select(Event))
    events = result.scalars().all()
    if events:
        return [event.to_dict() for event in events]
    return []


@router.post("/", name="create event", response_description="Create a new event")
async def create_event(_: Request, data: EventDto, session: AsyncSession = Depends(get_session)) -> dict:
    event = await get_row(session, Event, data.id)
    if event:
        return {'message': 'Event already exist', 'data': event.to_dict()}

    # remove time zone from date
    data.created_at = data.created_at.replace(tzinfo=None)
    event = Event(**data.dict(exclude_unset=True))
    session.add(event)
    await session.commit()

    return {"Message": "Event created"}


@router.put("/{event_id}", name="update event", response_description="Update a specific event by ID")
async def update_event(_: Request, event_id: str, data: EventDetailDto, session: AsyncSession = Depends(get_session)) -> dict:
    event = await get_row(session, Event, event_id)
    if not event:
        return {'message': 'Event not found'}

    stmt = update(Event).where(Event.id == event_id).values(**data.dict(exclude_unset=True))
    await session.execute(stmt)
    await session.commit()
    return {"Message": "Event updated"}


@router.delete("/{event_id}", name="delete event", response_description="Delete a specific event by ID")
async def delete_event(_: Request, event_id: str, session: AsyncSession = Depends(get_session)) -> dict:
    event : Event = await get_row(session, Event, event_id)
    if not event:
        return {'message': 'Event not found'}

    await session.delete(event)
    await session.commit()
    return {"message": "Event deleted"}
