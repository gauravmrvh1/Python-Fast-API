from pydantic import BaseModel, Field
from pydantic import ConfigDict

class UserResponse(BaseModel):
    user_id: int = Field(alias="id")
    name: str
    email: str
    mobile_number: int | None = None
    
    # model_config = ConfigDict(
    #     from_attributes=True,
    #     populate_by_name=True
    # )