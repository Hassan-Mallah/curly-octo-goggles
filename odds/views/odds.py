import httpx
from fastapi import APIRouter
from fastapi import Depends
from starlette.requests import Request
from fastapi import HTTPException
from fastapi import status
from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession

from .dto import OddsDto
from .dto import OddsDetailDto
from database.models import Odds
from database.models import OddsTypesEnum
from database.base import get_session
from database.base import get_row
from database.base import get_rows
from settings import settings

__all__ = ["router"]

router = APIRouter()


@router.get("/{event_id}/odds", name="get odds", response_description="Get odds for event by id")
async def get_event_by_id(_: Request, event_id: str, session: AsyncSession = Depends(get_session)) -> list:
    odds = await get_rows(session, Odds, event_id)
    if odds:
        return [Odds.to_dict(row) for row in odds]
    return []


@router.post("/{event_id}/odds", name="create event", response_description="Create a new event")
async def create_event(_: Request, event_id: str, data: OddsDto, session: AsyncSession = Depends(get_session)) -> dict:
    async with httpx.AsyncClient(timeout=5000) as client:
        response = await client.get(url=f"{settings.EVENTS_URL}/events/{event_id}")
        if response.status_code != 200:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event not found")

    if data.type not in OddsTypesEnum.types():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Type not found: {data.type}")

    odds = await get_row(session, Odds, data.id)
    if odds:
        return {'message': 'Odd already exist', 'data': odds.to_dict()}

    odds = Odds(event_id=event_id, **data.dict(exclude_unset=True))
    session.add(odds)
    await session.commit()

    return {"Message": "Odds created for the event"}


@router.put("/{event_id}/odds/{odds_id}", name="update odds", response_description="Update a specific odds by ID")
async def update_event(_: Request, event_id: str, odds_id: str, data: OddsDetailDto,
                       session: AsyncSession = Depends(get_session)) -> dict:
    row: Odds = await get_row(session, Odds, odds_id, update=True)

    # check odds id and event id are correct
    if not row or row.event_id != event_id:
        return {'message': 'Odds not found with this info'}

    if data.type and data.type not in OddsTypesEnum.types():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Type not found: {data.type}")

    stmt = update(Odds).where(Odds.id == odds_id).values(**data.dict(exclude_unset=True))
    await session.execute(stmt)
    await session.commit()
    return {"Message": "Event updated"}


@router.delete("/{event_id}/odds/{odds_id}", name="delete oods", response_description="Delete a specific odds by ID")
async def delete_event(_: Request, event_id: str, odds_id: str, session: AsyncSession = Depends(get_session)) -> dict:
    row: Odds = await get_row(session, Odds, odds_id)

    # check odds id and event id are correct
    if not row or row.event_id != event_id:
        return {'message': 'Odds not found with this info'}

    await session.delete(row)
    await session.commit()
    return {"message": "Odds deleted"}
