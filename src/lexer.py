# Dili analiz etme ve token'larına ayırmaktan sorumlu

class Lexer:
    tokenTypes = [
        "DEFINE_CLASS",
    ]

    def Tokenize(_inputCode: str, _levels: list):

        lines = [l.strip() for l in _inputCode.splitlines()]

        tokens = []

        for line in lines:
            start = 0
            end = 0
            newToken = []

            while end <= len(line):
                if line[start:end] == "sınıf":
                    newToken.append(Lexer.tokenTypes[0])
                    start = end

                    while end <= len(line):
                        if line[end-1:end] == "{":
                            newToken.append(line[start:end-1].strip())

                        end = end + 1
                else:
                    end = end + 1

            tokens.append(newToken)

        return tokens
