# Dili analiz etme ve token'larına ayırmaktan sorumlu
from classes.Line import Line
from classes.Pairs import pairs

from classes.Tokens import *

tokens = []  # ? Functions access this object so it has to be public


def Lexize(line: Line):
    pass


class Lexer:
    stringHashes = {}

    def Lex(_lines: list[Line]):
        global tokens
        lines = [l for l in _lines]

        # ? Hashing Strings
        for i, line in enumerate(lines):
            start = 0
            end = 0
            xline = line.value
            while end <= len(xline):
                if xline[end:end+1] == '"':
                    while '"' in xline:
                        start = xline.index('"')
                        xline = xline.replace('"', "", 1)
                        end = xline.index('"')
                        xline = xline.replace('"', "", 1)
                        Lexer.stringHashes[hash(xline[start: end])] = xline[start: end]
                        xline = xline.replace(xline[start: end], str(hash(xline[start: end])))
                end = end + 1

            lines[i].value = xline

        # ? Remove whitespaces
        for i, line in enumerate(lines):
            if line.value.replace(" ", "")[0:2] != "//":  # ? Yorum satırlarını olduğu gibi bırakması için böyle yaptım
                lines[i].value = line.value.replace(" ", "")

        # ? Lexing
        for line in lines:
            Lexize(line)  # ? Lexize is a function because recursion is needed

        return tokens


def Lexize(line: Line):
    _value = line.value

    # ? Var decleration
    if _value[0:8] == "değişken":
        if "=" in _value:  # ? Non-Null
            parts = _value.partition("=")
            tokens.append(VAR_DECLERATION(line.line, parts[0][8:], parts[2]))
        else:  # ? Null
            tokens.append(VAR_DECLERATION(line.line, _value[8:], None))
