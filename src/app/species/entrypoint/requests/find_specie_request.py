from typing import Optional
from pydantic import BaseModel

class FindSpecieRequest(BaseModel):
    name: Optional[str] = None