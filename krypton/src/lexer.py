# Dili analiz etme ve token'larına ayırmaktan sorumlu
from classes.Line import Line
from classes.Pairs import pairs


class Lexer:
    stringHashes = {}

    def Lex(_lines: list[Line]):

        lines = [l for l in _lines]

        # ? Hashing Strings
        for i, line in enumerate(lines):
            start = 0
            end = 0
            xline = line.value
            while end <= len(xline):
                if xline[end:end+1] == '"':
                    while '"' in xline:
                        start = xline.index('"')
                        xline = xline.replace('"', "", 1)
                        end = xline.index('"')
                        xline = xline.replace('"', "", 1)
                        Lexer.stringHashes[hash(xline[start: end])] = xline[start: end]
                        xline = xline.replace(xline[start: end], str(hash(xline[start: end])))
                end = end + 1

            lines[i].value = xline

        # ? Remove whitespaces
        for i, line in enumerate(lines):
            if line.value.replace(" ", "")[0:2] != "//":  # ? Yorum satırlarını olduğu gibi bırakması için böyle yaptım
                lines[i].value = line.value.replace(" ", "")

        # print(pairs)
        return lines
