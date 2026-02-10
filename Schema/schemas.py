from pydantic import BaseModel, Field
from typing import Optional

class User(BaseModel):
    name: str = Field(default="Gaurav", description="Full name of user")
    email: str = Field(default="gaurav@gmail.com")
    # aadhar_number: int = Field(...)
    aadhar_number: int | None=None
    # mobile_number: int | None = None
    mobile_number : Optional[int] = Field(
        default=None,
        description="Mobile number (optional)"
    )

class Admin(BaseModel):
    f_name: str = Field(default="Gaurav", description="Full name of user")
    l_name: str = Field(default="gaurav@gmail.com")
    username: int = Field(...)