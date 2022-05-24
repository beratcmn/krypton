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

VERSION = "0.0.1a"

debug = False
clear = False
dont_run = False
args = sys.argv[1:]  # ilk argüman kendisi olduğu için onu almıyoruz


def Help():
    # ? \033[F == \n tersi
    help_info = """...
Komut satırı argümanları:

--yardım --y: Yardım mesajını görüntüler.
--versiyon --v: Mevcut Krypton sürümünü görüntüler.
--çalıştırma --çm : Programı derledikten sonra dosyayı mevcut yola getirir ancak çalıştırmaz.
--debug --d: Programın derlenmeden önce geçtiği aşamaları gösterir. 
--temiz : Programı çalıştırmadan önce konsolu temizler.
"""
    print(help_info)


def Version():
    print("Krypton derleyicisi Versiyon: " + VERSION)


reserved_args = {
    "--yardım": Help,
    "--y": Help,
    "--versiyon": Version,
    "--v": Version
}


def Debug(input_lines, tokens, output_code):
    print("--- Input Lines ---")
    for _il in input_lines:
        print(_il)

    print("\n--- Tokens ---")
    for token in tokens:
        print(token)

    print("\n--- Output Code ---")
    print(output_code)
    print("-- Output Code End --")


def Clear(clear: bool):
    if clear:
        os.system("cls")


def CLI():
    global debug
    global clear
    global dont_run
    global args
    global reserved_args

    debug = "--debug" in args or "--d" in args

    clear = "--temiz" in args or "--t" in args

    dont_run = "--çalıştırma" in args or "--çm" in args

    if len(args) == 1:
        _arg = args[0]

        for _ra in reserved_args:
            if _arg == _ra:
                reserved_args[_ra]()
                sys.exit()

    Clear(clear)


def main():
    global debug
    global clear
    global dont_run
    global args

    CLI()

    input_file_path = str(args[0])

    input_file_name = input_file_path.split("\\")[-1]

    input_lines: list[Line] = Reader.ReadInputCode(input_file_path)

    tokens = Lexer.Lex(input_lines)

    pairs = []

    for i in range(len(input_lines)):
        pairs.append(Pair(input_lines[i], tokens[i]))

    output_code = Parser.Parse(pairs, input_file_name)

    Compiler.Compile(output_code, dont_run)

    if debug == True:
        Debug(input_lines, tokens, output_code)


if __name__ == "__main__":
    start = timeit.default_timer()
    main()
    stop = timeit.default_timer()
    print('\nDerleme Süresi:', stop - start, "saniye.")
