from pydantic import BaseModel


class Addition(BaseModel):
    additional_info: str | None = None
    additional_number: int | None = None


class ItemData(BaseModel):
    addition: Addition | None = None
    important_numbers: list[int] | None = None
    title: str | None = None
    verified: bool | None = None
    id: int | None = None
