from dataclasses import dataclass
from typing import Optional


@dataclass
class Option:
    text: str
    modal_id: Optional[str] = None
    value: Optional[str] = None
    field: Optional[str] = None

@dataclass
class Form:
    name: str
    question: str
    type: str
    options: list[Option] = None
    modal_id: Optional[str] = None
    field: Optional[str] = None
    another: bool = True