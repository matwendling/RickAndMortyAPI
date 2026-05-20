from typing import Optional
from pydantic import BaseModel

class FindLocationsRequest(BaseModel):
    name: Optional[str] = None