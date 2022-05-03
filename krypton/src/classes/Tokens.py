from dataclasses import dataclass


@dataclass
class Token:
    line: int


@dataclass
class VAR_DECLERATION(Token):
    name: str
    value: object
