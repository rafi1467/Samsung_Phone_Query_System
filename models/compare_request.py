from pydantic import BaseModel


class CompareRequest(BaseModel):
    phone1: str
    phone2: str