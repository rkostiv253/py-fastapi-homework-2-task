from pydantic import BaseModel

class GenreBase(BaseModel):
    title: str
    genre: str
    price: float

class GenreCreate(GenreBase):
    pass

class GenreUpdate(GenreBase):
    pass

class GenreRead(GenreBase):
    id: int

    class Config:
        from_attributes = True