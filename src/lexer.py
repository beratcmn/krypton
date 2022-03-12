# Dili analiz etme ve token'larına ayırmaktan sorumlu

from dataclasses import dataclass
from reader import PreToken


class Token:
    level: int


class Lexer:
    def Lex(preTokens: list[PreToken]) -> list[Token]:
        pass
