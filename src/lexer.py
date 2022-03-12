# Dili analiz etme ve token'larına ayırmaktan sorumlu

from dataclasses import dataclass
from unicodedata import name
from reader import PreToken

import enum
import re


@dataclass
class Type:
    name: str
    pattern: str


@dataclass
class Token:
    level: int
    lineNumber: int
    originalValue: str
    type: str = ""
    value: str = ""

    def __post_init__(self):
        types = [
            Type(name="VAR_ASSIGN_LONG", pattern="değişken [a-zA-Z0-9_]+ = .*"),
            Type(name="VAR_ASSIGN_SHORT", pattern="değ [a-zA-Z0-9_]+ = .*"),
            Type(name="FUNC_CREATE_LONG", pattern="fonksiyon [a-zA-Z0-9_]+\(.*\)"),
            Type(name="FUNC_CREATE_SHORT", pattern="f [a-zA-Z0-9_]+\(.*\)"),
        ]

        for type in types:
            if len((re.findall(type.pattern, self.originalValue))) > 0:
                self.type = type.name
                break


class Lexer:

    def Lex(preToken: PreToken) -> Token:
        pass

    def Analize(preTokens: list[PreToken]) -> list[Token]:
        tokens = []

        for pre_token in preTokens:
            tokens.append(Token(level=pre_token.level, lineNumber=pre_token.lineNumber, originalValue=pre_token.value))

        for token in tokens:
            print(token)
