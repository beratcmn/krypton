# Programı okuyup düzgün hale getirmekten sorumlu


class Reader:
    def ReadInputCode():
        #input_file = open("gramer.kr", "r", encoding="utf-8")
        input_file = open(
            r'C:\Users\\berat\Projects\Python\krypton-beta\gramer\gramer1.kr',
            "r", encoding="utf-8")  # ? Debug

        input_code = input_file.read().rstrip()

        lines = input_code.splitlines()
        line_count = len(lines)
        currentLevel = 0
        levels = []
        for i in range(0, line_count):
            levels.append([i, currentLevel])

            if "{" in lines[i]:
                currentLevel = currentLevel + 1
            if "}" in lines[i]:
                currentLevel = currentLevel - 1

        # for i in levels:
        #     print(i)

        input_file.close()

        return input_code, levels
