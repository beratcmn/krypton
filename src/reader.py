# Programı okuyup düzgün hale getirmekten sorumlu


class Reader:
    def ReadInputCode(filePath: str):
        #input_file = open("gramer.kr", "r", encoding="utf-8")
        input_file = open(filePath, "r", encoding="utf-8")  # ? Debug

        input_code = input_file.read().rstrip()

        lines = [l.strip() for l in input_code.splitlines()]
        currentLevel = 0
        levels = []

        for line in lines:
            if line == "}":
                levels.append([lines.index(line), currentLevel - 1])
            else:
                levels.append([lines.index(line), currentLevel])

            if "{" in line:
                currentLevel = currentLevel + 1
            if "}" in line:
                currentLevel = currentLevel - 1

        input_file.close()

        return input_code, levels
