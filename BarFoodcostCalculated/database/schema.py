from pydantic import BaseModel

class Alcohol(BaseModel):
    id: int
    name: str
    volume: int
    price: float

    class Config:
        orm_mode = True