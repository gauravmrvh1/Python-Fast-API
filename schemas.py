from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    mobile_number : int
    # age: int | None = None
