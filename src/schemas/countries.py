from pydantic import BaseModel

class CountryBase(BaseModel):
    title: str
    genre: str
    price: float

class CountryCreate(CountryBase):
    pass

class CountryUpdate(CountryBase):
    pass

class CountryRead(CountryBase):
    id: int

    class Config:
        from_attributes = True