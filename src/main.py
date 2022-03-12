# Bütün her şeyi birleştirmekten sorumlu

from reader import Reader
from lexer import Lexer
from compiler import Compiler
from writer import Writer

from reader import PreToken
from lexer import Token


def main():
    pre_tokens = Reader.Read()
    tokens = Lexer.Analize(pre_tokens)

    # print(tokens)


if __name__ == "__main__":
    main()
