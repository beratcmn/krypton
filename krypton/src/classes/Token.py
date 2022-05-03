from dataclasses import dataclass


@dataclass
class Token:
    line: int
    # level: int
    type: str
    value: object
