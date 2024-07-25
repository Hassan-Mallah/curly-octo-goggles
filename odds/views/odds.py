import httpx
from fastapi import APIRouter
from fastapi import Depends
from starlette.requests import Request
from fastapi import HTTPException
from fastapi import status
from sqlalchemy import select
from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession

from .dto import OddsDto
from .dto import OddsDetailDto
from database.models import Odds
from database.models import OddsTypesEnum
from database.base import get_session
from database.base import get_row

__all__ = ["router"]

router = APIRouter()


# @router.get("/{event_id}", name="get event", response_description="Get event by id")
# async def get_event_by_id(_: Request, event_id: str, session: AsyncSession = Depends(get_session)) -> dict:
#     event = await get_row(session, Event, event_id)
#     if event:
#         return Event.to_dict(event)
#     else:
#         return {'message': 'Event not found'}
#

@router.post("/{event_id}/odds", name="create event", response_description="Create a new event")
async def create_event(_: Request, event_id: str, data: OddsDto, session: AsyncSession = Depends(get_session)) -> dict:
    async with httpx.AsyncClient(timeout=5000) as client:
        response = await client.get(url=f"http://:5000/events/{event_id}")
        if response.status_code != 200:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event not found")

    if data.type not in OddsTypesEnum.types():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Status not found")

    odds = await get_row(session, Odds, data.id)
    if odds:
        return {'message': 'Odd already exist', 'data': odds.to_dict()}

    odds = Odds(event_id=event_id, **data.dict(exclude_unset=True))
    print(odds.to_dict())
    session.add(odds)
    await session.commit()

    return {"Message": "Odd created for the event"}


# @router.put("/{event_id}", name="update event", response_description="Update a specific event by ID")
# async def update_event(_: Request, event_id: str, data: EventDetailDto,
#                        session: AsyncSession = Depends(get_session)) -> dict:
#     event = await get_row(session, Event, event_id)
#     if not event:
#         return {'message': 'Event not found'}
#
#     stmt = update(Event).where(Event.id == event_id).values(**data.dict(exclude_unset=True))
#     await session.execute(stmt)
#     await session.commit()
#     return {"Message": "Event updated"}
#
#
# @router.delete("/{event_id}", name="delete event", response_description="Delete a specific event by ID")
# async def delete_event(_: Request, event_id: str, session: AsyncSession = Depends(get_session)) -> dict:
#     event: Event = await get_row(session, Event, event_id)
#     if not event:
#         return {'message': 'Event not found'}
#
#     await session.delete(event)
#     await session.commit()
#     return {"message": "Event deleted"}
