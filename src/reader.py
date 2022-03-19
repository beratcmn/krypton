# Programı okuyup düzgün hale getirmekten sorumlu


class Reader:
    def ReadInputCode():
        #input_file = open("gramer.kr", "r", encoding="utf-8")
        input_file = open(
            r'C:\Users\\berat\Projects\Python\krypton-beta\gramer\gramer1.kr',
            "r", encoding="utf-8")  # ? Debug

        input_code = input_file.read().rstrip()

        input_file.close()

        return input_code
