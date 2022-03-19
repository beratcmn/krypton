# Bütün her şeyi birleştirmekten sorumlu

from reader import Reader
from lexer import Lexer
from compiler import Compiler
from writer import Writer


def main():
    print(Reader.ReadInputCode())


if __name__ == "__main__":
    main()
