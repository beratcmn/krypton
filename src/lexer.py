# Dili analiz etme ve token'larına ayırmaktan sorumlu


class Lexer:
    debug = False

    tokenTypes = [
        "DEFINE_CLASS",         # 0
        "DEFINE_FUNCTION",      # 1
        "INVOKE_FUNCTION",      # 2
        "VAR_ASSIGN",           # 3
        "VAR_ASSIGN_NULL",      # 4
        "IF",                   # 5
        "ELSE_IF",              # 6
        "ELSE",                 # 7
    ]

    reserved = [
        "fonksiyon",
        "eğer",
        "değilse ve",
        "değilseve",
        "değilse",
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

        # ? Remove whitespaces
        for i, line in enumerate(lines):
            if line.replace(" ", "")[0:2] != "//":  # ? Yorum satırlarını olduğu gibi bırakması için böyle yaptım
                lines[i] = line.replace(" ", "")

        if Lexer.debug == True:
            print("Without whitespaces:")
            for line in lines:
                print(line)

        # ? Parsing
        for line in lines:
            start = 0
            end = 0
            newToken = []

            while end <= len(line):
                end = end + 1

                # ? Full line Comment
                if line[0:2] == "//":
                    newToken.append("FULL_COMMENT")
                    newToken.append(line.replace("//", "", 1))
                    break

                # ? Brackets
                if line == "{":
                    newToken.append("{")
                    break
                if line == "}":
                    newToken.append("}")
                    break
                if line == "":
                    newToken.append("")
                    break

                # ? Var Assign
                if line[start:end] == "değişken":
                    start = end

                    # ? Find var name
                    if "=" in line:
                        newToken.append(Lexer.tokenTypes[3])
                        newToken.append(line[start:len(line)-1].partition("=")[0].strip())
                        newToken.append(line[start:len(line)-1].partition("=")[2].strip())
                    else:
                        newToken.append(Lexer.tokenTypes[4])
                        newToken.append(line[start:len(line)-1].partition("değişken")[0].strip())
                    break

                # ? Class
                if line[start:end] == "sınıf":
                    start = end
                    newToken.append(Lexer.tokenTypes[0])
                    newToken.append(line.partition("sınıf")[2].strip().replace("{", ""))
                    break

                # ? Define function
                if line[start:end] == "fonksiyon":
                    start = end
                    newToken.append(Lexer.tokenTypes[1])

                    while end <= len(line):
                        end = end + 1

                        # ? Find function name
                        if line[end:end+1] == "(":
                            newToken.append(line[start:end].strip())
                            start = end

                        # ? Find props
                        if line[end-1:end] == ")":
                            newToken.append(line[start+1:end-1].strip())
                            start = end
                    break

                # ? Invoke Function
                if line[start:end].strip() not in Lexer.reserved and line[end:end+1] == "(" and line[start:end] != " " and line[start:end] != "":
                    newToken.append(Lexer.tokenTypes[2])
                    newToken.append(line[start:end])
                    start = end

                    while end <= len(line):
                        end = end + 1
                        # ? Find props
                        if line[end-1:end] == ")":
                            newToken.append(line[start+1:end-1].strip())
                            start = end

                # ? If
                if line[start:end] == "eğer":
                    start = end
                    newToken.append(Lexer.tokenTypes[5])
                    newToken.append(line.partition("eğer")[2].strip().replace("{", ""))
                    break

                # ? Else If
                if line[start:end] == "değilseve":
                    start = end
                    newToken.append(Lexer.tokenTypes[6])
                    newToken.append(line.partition("değilseve")[2].strip().replace("{", ""))
                    break

                # ? Else
                if line[start:end] == "değilse" and line[start:end + 2] != "değilseve":
                    start = end
                    newToken.append(Lexer.tokenTypes[7])
                    break

            tokens.append(newToken)
        return tokens, Lexer.stringHashes
