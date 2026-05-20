from typing import Optional
from pydantic import BaseModel

class FindOriginsRequest(BaseModel):
    name: Optional[str] = None