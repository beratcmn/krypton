# Tokenleri işlenebilir hale getirmekten sorumlu
from classes.Tokens import *
from classes.Pair import Pair


def ParsePair(pair: Pair):
    pass


def ParseToken(token: Token):
    pass


class Parser:
    def Parse(pairs: list[Pair]) -> str:
        output_code = ""

        for pair in pairs:
            line = ParsePair(pair)
            output_code = output_code + str(line) + "\n"

        return output_code


def ParsePair(pair: Pair):
    if isinstance(pair.token, VAR_DECLERATION):
        line = pair.line.level * " " + pair.token.name + " = " + ParseToken(pair.token.value)
        return line
    elif isinstance(pair.token, INVOKE_FUNCTION):
        function_name = pair.token.function_name
        if pair.token.function_name == "yazdır":
            function_name = "print"
        elif pair.token.function_name == "karekök":
            function_name = "print"  # ! CHANGE LATER
        else:
            function_name = pair.token.function_name

        line = pair.line.level * " " + function_name + "("

        for p in pair.token.function_params:
            if pair.token.function_params.index(p) != len(pair.token.function_params) - 1:
                line = line + ParseToken(p) + ", "
            else:
                line = line + ParseToken(p)

        line = line + ")"
        return line


def ParseToken(token: Token):
    if isinstance(token, INVOKE_FUNCTION):
        token: INVOKE_FUNCTION = token

        function_name = token.function_name
        if token.function_name == "yazdır":
            function_name = "print"
        elif token.function_name == "karekök":
            function_name = "print"  # ! CHANGE LATER
        else:
            function_name = token.function_name

        word = function_name + "("
        for p in token.function_params:
            if token.function_params.index(p) != len(token.function_params) - 1:
                word = word + str(p) + ", "
            else:
                word = word + str(p)
        word = word + ")"
        return str(word)
    return str(token)
