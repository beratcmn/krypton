# Programı derlemekten sorumlu
import os
import subprocess


class Compiler:
    def Compile(_input: str, _dont_run: bool):
        folder_directory = os.environ['USERPROFILE'] + "\\.krypton_cache\\"
        is_dir_exists = os.path.isdir(folder_directory)

        if is_dir_exists == False:
            path = os.path.join(os.environ['USERPROFILE'], ".krypton_cache")
            os.mkdir(path)

        file_directory = folder_directory + "cache.py"

        cache_file = open(file_directory, "w+", encoding="utf-8")
        cache_file.write(_input)
        cache_file.close()

        if _dont_run == False:
            subprocess.call(["python", file_directory])

        # exec(program)
