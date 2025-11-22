from pydantic import BaseModel

class LanguageBase(BaseModel):
    title: str
    genre: str
    price: float

class LanguageCreate(LanguageBase):
    pass

class LanguageUpdate(LanguageBase):
    pass

class LanguageRead(LanguageBase):
    id: int

    class Config:
        from_attributes = True