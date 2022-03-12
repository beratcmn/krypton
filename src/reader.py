# Programı okuyup düzgün hale getirmekten sorumlu

from dataclasses import dataclass


@dataclass
class PreToken:
    level: int
    lineNumber: int
    value: str


class Reader:
    def Read() -> list[PreToken]:
        input_file = open("gramer.kr", "r", encoding="utf-8")
        input_lines = [line.rstrip("\n") for line in input_file.readlines()]

        tokens = []

        i = 1
        for line in input_lines:
            tokens.append(PreToken(level=line.count("    "), lineNumber=i, value=line.replace("    ", "")))
            i = i + 1

        input_file.close()

        return tokens
