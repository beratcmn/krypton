# Programı okuyup düzgün hale getirmekten sorumlu

from dataclasses import dataclass
import re


@dataclass
class PreToken:
    level: int
    value: str


class Reader:
    def Read() -> list[PreToken]:
        input_file = open("gramer.kr", "r", encoding="utf-8")
        input_lines = [line.rstrip("\n") for line in input_file.readlines()]

        tokens = []

        for line in input_lines:
            tokens.append(PreToken(line.count("    "), line.replace("    ", "")))

        input_file.close()

        return tokens
