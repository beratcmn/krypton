# Bütün her şeyi birleştirmekten sorumlu

from reader import Reader
from lexer import Lexer
from parser import Parser
from compiler import Compiler
from writer import Writer
from shell import Shell


def ShowTokens(tokens, levels):
    for i in range(0, len(tokens)):
        print(str(i+1) + ": " + str(tokens[i]) + " Level: " + str(levels[i][1]))


def main():
    input_code, levels = Reader.ReadInputCode()
    tokens, string_hashes = Lexer.Tokenize(_inputCode=input_code, _levels=levels)
    parsed_code = Parser.Parse(tokens, levels, string_hashes)

    print("Source Code:")
    print(input_code)
    print("\nLex Result:")
    ShowTokens(tokens, levels)
    print("\nParse Result:")
    print(parsed_code)


if __name__ == "__main__":
    main()
