from dataclasses import dataclass
from classes.Tokens import *
from classes.Line import Line


@dataclass
class Pair:
    line: Line
    token: object
