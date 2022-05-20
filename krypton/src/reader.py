# Programı okuyup düzgün hale getirmekten sorumlu
from classes.Line import Line


class Reader:
    def ReadInputCode(filePath: str):
        input_file = open(filePath, "r", encoding="utf-8")  # ? Debug

        input_code = input_file.read().rstrip()

        lines = [l.strip() for l in input_code.splitlines()]
        currentLevel = 0
        levels = []

        lineObjects = []

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

        for i in range(len(lines)):
            lineObjects.append(Line(i, levels[i][1] + 0, lines[i]))

        return lineObjects
