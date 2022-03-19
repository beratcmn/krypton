# Bütün her şeyi birleştirmekten sorumlu

from reader import Reader
from lexer import Lexer
from compiler import Compiler
from writer import Writer


def main():
    input_code = Reader.ReadInputCode()[0]
    levels = Reader.ReadInputCode()[1]
    tokens = Lexer.Tokenize(_inputCode=input_code, _levels=levels)

    for i in range(0, len(tokens)):
        print(str(i+1) + ": " + str(tokens[i]) + " Level: " + str(levels[i][1]))


if __name__ == "__main__":
    main()
