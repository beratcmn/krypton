# Bütün her şeyi birleştirmekten sorumlu

from reader import Reader
from lexer import Lexer
from parser import Parser
from compiler import Compiler
from writer import Writer
from shell import Shell

import sys

debug = False

reserved_args = [
    "--çalıştırma",
]


def ShowTokens(tokens, levels):
    for i in range(0, len(tokens)):
        print(str(i+1) + ": " + str(tokens[i]) + " Level: " + str(levels[i][1]))


def main():
    global debug
    global reserved_args

    args = sys.argv[1:]  # ilk argüman kendisi olduğu için onu almıyoruz

    input_file_path = str(args[0])

    inputLines = Reader.ReadInputCode(input_file_path)

    tokens = Lexer.Lex(inputLines)

    for token in tokens:
        print(token)


if __name__ == "__main__":
    main()
