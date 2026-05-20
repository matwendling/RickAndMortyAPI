from typing import Optional

from pydantic import BaseModel

class FindClassificationTypesRequest(BaseModel):
    name: Optional[str] = None