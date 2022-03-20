# Programı derlemekten sorumlu

import subprocess


class Compiler:
    def Compile(_input: str):
        file_directory = __file__
        file_directory = file_directory.replace("compiler.py", "") + "cache\\cache.py"
        cache_file = open(file_directory, "w+", encoding="utf-8")
        cache_file.write(_input)
        cache_file.close()

        subprocess.call(["python", file_directory])

        # exec(program)
