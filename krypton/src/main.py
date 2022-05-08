#!/usr/bin/env python3
# Bütün her şeyi birleştirmekten sorumlu

from reader import Reader
from lexer import Lexer
from parser import Parser
from compiler import Compiler
from writer import Writer
from shell import Shell

from classes.Line import Line
from classes.Pair import Pair

import timeit
import sys
import os

debug = False
clear = False

reserved_args = [
    "--debug",
    "--çalıştırma",
    "--temiz",
]


def Debug(input_lines, tokens):
    print("--- Input Lines ---")
    for _il in input_lines:
        print(_il)

    print("\n--- Tokens ---")
    for token in tokens:
        print(token)


def Clear(clear: bool):
    if clear:
        os.system("cls")


def main():
    global debug
    global clear
    args = sys.argv[1:]  # ilk argüman kendisi olduğu için onu almıyoruz

    debug = "--debug" in args

    clear = "--temiz" in args

    Clear(clear)

    input_file_path = str(args[0])

    input_lines: list[Line] = Reader.ReadInputCode(input_file_path)

    tokens = Lexer.Lex(input_lines)

    pairs = []

    for i in range(len(input_lines)):
        pairs.append(Pair(input_lines[i], tokens[i]))

    output_code = Parser.Parse(pairs)

    if debug == True:
        Debug(input_lines, tokens)


if __name__ == "__main__":
    start = timeit.default_timer()
    main()
    stop = timeit.default_timer()
    print('\nDerleme Süresi:', stop - start, "saniye.")
