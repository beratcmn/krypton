# Programı derlemekten sorumlu
import os
import subprocess

from os.path import exists
import shutil


class Compiler:
    def Compile(_input: str, _dont_run: bool):
        folder_directory = str(os.environ['USERPROFILE'] + "/.krypton_cache/").replace("\\", "/")
        is_dir_exists = os.path.isdir(folder_directory)

        if is_dir_exists == False:
            path = os.path.join(os.environ['USERPROFILE'], ".krypton_cache")
            os.mkdir(path)

        file_directory = folder_directory + "program.py"

        if exists(folder_directory + "executer.py") == False:
            shutil.copyfile(os.getcwd() + "/krypton/src/resources/executer.py", folder_directory + "executer.py")

        if exists(folder_directory + "mithen.py") == False:
            shutil.copyfile(os.getcwd() + "/krypton/src/resources/mithen.py", folder_directory + "mithen.py")

        cache_file = open(file_directory, "w+", encoding="utf-8")
        cache_file.write(_input)
        cache_file.close()

        if _dont_run == False:
            subprocess.call(["python", folder_directory + "executer.py"])

        # exec(program)
