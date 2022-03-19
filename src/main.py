# Bütün her şeyi birleştirmekten sorumlu

from reader import Reader
from lexer import Lexer
from compiler import Compiler
from writer import Writer


def main():
    input_code = Reader.ReadInputCode()[0]
    levels = Reader.ReadInputCode()[1]
    tokens = Lexer.Tokenize(_inputCode=input_code, _levels=levels)

    for t in tokens:
        print(t)


if __name__ == "__main__":
    main()
