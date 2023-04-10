from pydantic import BaseModel, Field


class User(BaseModel):
    email: str = Field(min_length=5, max_length=50)
    password: str = Field(min_length=5, max_length=50)

    class Config:
        schema_extra = {
            "example": {
                "email": "admin@gmail.com",
                "password": "admin"
            }
        }
