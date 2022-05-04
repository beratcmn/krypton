#!/usr/bin/env python3
# Bütün her şeyi birleştirmekten sorumlu

from reader import Reader
from lexer import Lexer
from parser import Parser
from compiler import Compiler
from writer import Writer
from shell import Shell

from classes.Line import Line

import timeit
import sys
import os

debug = True

reserved_args = [
    "--çalıştırma",
]


def Debug(input_lines, tokens):
    print("--- Input Lines ---")
    for _il in input_lines:
        print(_il)

    print("\n--- Tokens ---")
    for token in tokens:
        print(token)


def main():
    global debug
    global reserved_args

    if debug:
        os.system("cls")  # ? Windows Only

    args = sys.argv[1:]  # ilk argüman kendisi olduğu için onu almıyoruz

    input_file_path = str(args[0])

    input_lines: list[Line] = Reader.ReadInputCode(input_file_path)

    tokens = Lexer.Lex(input_lines)

    if debug == True:
        Debug(input_lines, tokens)


if __name__ == "__main__":
    start = timeit.default_timer()
    main()
    stop = timeit.default_timer()
    print('\nDerleme Süresi:', stop - start, "saniye")
