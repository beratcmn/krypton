# Dili analiz etme ve token'larına ayırmaktan sorumlu
from classes.Line import Line
from classes.Pairs import pairs

from classes.Tokens import *


def Lexize(line: Line):
    pass


class Lexer:
    stringHashes = {}

    def Lex(_lines: list[Line]):

        lines = [l for l in _lines]
        tokens = []

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
            tokens.append(Lexize(line))  # ? Lexize is a function because recursion is needed

        return tokens


def Lexize(line: Line) -> Token:
    _value = line.value
    _value = _value.replace("{", "").replace("}", "")

    # ? Var Decleration
    if _value[0:8] == "değişken":
        if "=" in _value:  # ? Non-Null
            parts = _value.partition("=")
            var_value = Lexize(Line(-1, -1, parts[2]))  # ? When line and level are == -1 means its on the same line
            return VAR_DECLERATION(line.line, parts[0][8:], var_value)
        else:  # ? Null
            return VAR_DECLERATION(line.line, _value[8:], None)

    # ? Var Assign
    if "=" in _value and "==" not in _value:
        parts = _value.partition("=")
        return VAR_ASSIGN(line.line, parts[0], Lexize(Line(-1, -1, parts[2])))

    # ? Define Function
    if _value[0:9] == "fonksiyon" or _value[0:2] == "fn":
        if _value[0:9] == "fonksiyon":
            _value = _value[9:]
            parts = _value.partition("(")
            params = parts[2][:-1].split(",")
            return DEFINE_FUNCTION(line.line, parts[0], params)
        elif _value[0:2] == "fn":
            _value = _value[2:]
            parts = _value.partition("(")
            return DEFINE_FUNCTION(line.line, parts[0], parts[2][:-1])

    # ? If
    if _value[0:4] == "eğer":
        _value = _value[4:]
        condition_string = _value[1:-1]

        parts = []
        newCondition = CONDITION(None, None, None)

        if ">" in condition_string:
            parts = condition_string.partition(">")
            newCondition.operator = ">"
        elif "<" in condition_string:
            parts = condition_string.partition("<")
            newCondition.operator = "<"
        elif "==" in condition_string:
            parts = condition_string.partition("==")
            newCondition.operator = "=="
        elif "!=" in condition_string:
            parts = condition_string.partition("!=")
            newCondition.operator = "!="

        newCondition.first = Lexize(Line(-1, -1, parts[0]))
        newCondition.second = Lexize(Line(-1, -1, parts[2]))

        return IF(line.line, newCondition)

    # ? Invoke Function
    if (_value[0:9] != "fonksiyon" or _value[0:2] != "fn") and "(" in _value:
        parts = _value.partition("(")
        params_str = parts[2][:-1].split(",")
        param_objects = []

        for p in params_str:
            param_objects.append(Lexize(Line(-1, -1, p)))

        return INVOKE_FUNCTION(line.line, parts[0], param_objects)

    return _value
