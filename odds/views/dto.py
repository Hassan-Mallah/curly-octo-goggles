from datetime import datetime
from pydantic import BaseModel

__all__ = ['OddsDto', 'OddsDetailDto']


class OddsDto(BaseModel):
    id: str
    type: str
    value: int


class OddsDetailDto(BaseModel):
    type: str
    value: int
