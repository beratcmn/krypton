# Dili analiz etme ve token'larına ayırmaktan sorumlu

from dataclasses import dataclass
from unicodedata import name
from reader import PreToken

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
            Type(name="VAR_ASSIGN_LONG", pattern="değişken [a-zA-Z0-9_ığüşiöç]+ = .*"),
            Type(name="VAR_ASSIGN_SHORT", pattern="değ [a-zA-Z0-9_ığüşiöç]+ = .*"),
            Type(name="FUNC_CREATE_LONG", pattern="fonksiyon [a-zA-Z0-9_ığüşiöç]+\(.*\)"),
            Type(name="FUNC_CREATE_SHORT", pattern="f [a-zA-Z0-9_ığüşiöç]+\(.*\)"),
            # ! IMPROVE FUNC_INVOKE | test_patern = (?<!fonksiyon +)[a-zA-Z0-9_ığüşiöç]+\(.*\)
            Type(name="FUNC_INVOKE", pattern="[a-zA-Z0-9_ığüşiöç]+\(.*\)"),
            Type(name="IF_OPERATION", pattern="eğer *\(.+\)"),
            Type(name="ELIF_OPERATION", pattern="değilse ve *\(.+\)"),
            Type(name="ELSE_OPERATION", pattern="değilse(?! )"),
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

        return tokens
