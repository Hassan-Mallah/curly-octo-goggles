from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy import func
from .base import Base


class Event(Base):
    __tablename__ = "events"

    id = Column(String, primary_key=True)
    name = Column(String)
    location = Column(String)
    teams = Column(ARRAY(String))
    created_at: datetime = Column(
        DateTime,
        default=datetime.utcnow,
        server_default=func.current_timestamp(),
    )

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location,
            'teams': self.teams,
            'created_at': self.created_at,
        }
