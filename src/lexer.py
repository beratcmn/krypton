# Dili analiz etme ve token'larına ayırmaktan sorumlu

class Lexer:
    tokenTypes = [
        "DEFINE_CLASS",         # 0
        "CREATE_FUNCTION",      # 1
        "INVOKE_FUNCTION",      # 2
        "COMMENT",              # 3
    ]

    stringHashes = {}

    def Tokenize(_inputCode: str, _levels: list):

        lines = [l.strip() for l in _inputCode.splitlines()]

        tokens = []

        # ? String hashes
        for line in lines:
            start = 0
            end = 0
            xline = line
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

            lines[lines.index(line)] = xline

        for line in lines:
            start = 0
            end = 0
            newToken = []

            while end <= len(line):

                # ? Comments
                if line[start:end] == "//":
                    newToken.append(Lexer.tokenTypes[3])
                    newToken.append(line[2:len(line)].strip())
                    break

                # ? Brackets
                if line == "{":
                    newToken.append("LEFT_BRACKET")
                    newToken.append("{")
                    break
                if line == "}":
                    newToken.append("RIGHT_BRACKET")
                    newToken.append("}")
                    break

                # ? Class
                if line[start:end] == "sınıf":
                    newToken.append(Lexer.tokenTypes[0])
                    newToken.append(line.partition("sınıf")[2].replace("{", "").strip())
                    break

                # ? Def
                if line[start:end] == "fonksiyon":
                    newToken.append(Lexer.tokenTypes[1])
                    start = end

                    while end <= len(line):
                        if line[end-1:end] == "(":
                            newToken.append(line[start:end-1].strip())

                            start = end
                            while line[end-1:end] != ")":
                                end = end + 1

                            newToken.append(line[start:end-1].split(","))  # ? props

                        end = end + 1

                # ? Invoke Def
                if line[start:end] != "fonksiyon" and line[end-1:end] == "(":
                    newToken.append(Lexer.tokenTypes[2])
                    newToken.append(line[start:end-1])
                    start = end
                    while line[end-1:end] != ")":
                        end = end + 1

                    newToken.append(line[start:end-1].split(","))  # ? props

                end = end + 1

            tokens.append(newToken)
        return tokens
