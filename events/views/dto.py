from datetime import datetime
from decimal import Decimal
from typing import Any
from typing import Literal

from fastapi import Form
from pydantic import UUID4
from pydantic import BaseModel
from pydantic import Field
from pydantic import validator


class EventDto(BaseModel):
    id: str
    name: str
    location: str | None = None
    teams: list | None = None
    created_at: datetime