from pydantic import BaseModel
from typing import List, Optional

class EmailModel(BaseModel):
    From: str
    To: List[str]
    Bcc: Optional[List[str]] = []
    Cc: Optional[List[str]] = []
    Subject: str
    Body: str