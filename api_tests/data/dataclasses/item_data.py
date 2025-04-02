from typing import Optional, List

from pydantic import BaseModel


class Addition(BaseModel):
    additional_info: Optional[str] = None
    additional_number: Optional[int] = None


class ItemData(BaseModel):
    addition: Optional[Addition] = None
    important_numbers: List[int] | None = None
    title: Optional[str] = None
    verified: Optional[bool] = None

# # pydantic version
# from pydantic import BaseModel
#
# class Addition(BaseModel):
#     additional_info: str | None = None
#     additional_number: int | None = None
#
# class ItemData(BaseModel):
#     addition: Addition | None = None
#     important_numbers: list[int] | None = None
#     title: str | None = None
#     verified: bool | None = None
#     id: int | None = None  # Добавляем, если API возвращает ID
