from pydantic import BaseModel


class PongResponseSchema(BaseModel):
    ping: str
    environment: str
    testing: bool
