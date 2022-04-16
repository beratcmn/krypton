from dataclasses import dataclass


@dataclass
class Token:
    level: int
    type: str
    value: object
