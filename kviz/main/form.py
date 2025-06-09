from dataclasses import dataclass
from typing import Optional


@dataclass
class Option:
    text: str
    next: Optional[str] = None
    value: Optional[str] = None
    field: Optional[str] = None


@dataclass
class Form:
    name: str
    title: str
    type: str
    options: list[Option] = None
    next: Optional[str] = None
    field: Optional[str] = None
    another: bool = True
    another_field: Optional[str] = None