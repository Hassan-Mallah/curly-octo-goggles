from datetime import datetime
import enum

from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import DateTime
from sqlalchemy import Enum
from .base import Base

__all__ = ["Odds"]


class OddsTypesEnum(enum.StrEnum):
    win = "win"
    lose = "lose"
    draw = "draw"

    @classmethod
    def types(cls):
        """get names of all types"""
        return cls._member_names_


class Odds(Base):
    __tablename__ = "odds"

    id = Column(String, primary_key=True)
    event_id = Column(String)
    type = Column(Enum(*OddsTypesEnum.types(), name='type_choices'))  # get values from enum
    value = Column(Integer)
    created_at: datetime = Column(
        DateTime,
        default=datetime.utcnow,
    )

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'event_id': self.event_id,
            'type': self.type,
            'value': self.value,
            'created_at': self.created_at,
        }
