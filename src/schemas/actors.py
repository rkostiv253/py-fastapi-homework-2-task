from pydantic import BaseModel

class ActorBase(BaseModel):
    title: str
    genre: str
    price: float

class ActorCreate(ActorBase):
    pass

class ActorUpdate(ActorBase):
    pass

class ActorRead(ActorBase):
    id: int

    class Config:
        from_attributes = True