from pydantic import BaseModel, Field

class ResponseModel(BaseModel):
    """
    General response model
    """
    id: int

    class Config:
        orm_mode = True