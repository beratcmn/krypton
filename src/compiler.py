# Programı derlemekten sorumlu

import os


class Compiler:
    def Compile(_input: str):
        file_directory = __file__
        file_directory = file_directory.replace("compiler.py", "") + "cache\\cache.py"
        cache_file = open(file_directory, "w+", encoding="utf-8")
        cache_file.write(_input)
        cache_file.close()

        program = open(file_directory, "r", encoding="utf-8").read()

        exec(program)
