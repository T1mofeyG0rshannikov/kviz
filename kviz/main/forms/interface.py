from dataclasses import dataclass
from typing import Optional


@dataclass
class OptionI:
    text: str
    next: Optional[str] = None
    field: Optional[str] = None


@dataclass
class FormI:
    name: str
    title: str
    type: str
    max_steps: int = 1
    options: list[OptionI] = None
    next: Optional['FormI'] = None
    another_field: Optional[str] = None
    options_count: int = 0
    show_next: bool = False


    def __hash__(self):
        return hash(self.name)