from typing import Optional
from pydantic import BaseModel

class Property(BaseModel):
    id: Optional[int] = None
    name: str
    type: str
    city: str
    price: float
    description: str
    ownerName: str
    createdAt: str