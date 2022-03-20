# Tokenleri işlenebilir hale getirmekten sorumlu

class Parser:
    def Parse(_tokens: list, _levels: list, _string_hashes: dict) -> str:
        parsed_lines = []
        output_code = ""

        for i, token in enumerate(_tokens):
            line = ""
            # ? Parse Class
            if token[0] == "DEFINE_CLASS":
                line = int(_levels[i][1]) * "    " + "class " + token[1] + ":"

            # ? Parse Comment
            elif token[0] == "FULL_COMMENT":
                line = int(_levels[i][1]) * "    " + "#" + token[1]

            # ? Parse Main Function Definition
            elif token[0] == "DEFINE_FUNCTION" and token[1] == "Giriş":
                line = int(_levels[i][1]) * "    " + "def Main" + "(" + token[2] + ")" + ":"

            # ? Parse Normal Function Definition
            elif token[0] == "DEFINE_FUNCTION":
                line = int(_levels[i][1]) * "    " + "def " + token[1] + "(" + token[2] + ")" + ":"

            # ? Parse Print Function Invoke
            elif token[0] == "INVOKE_FUNCTION" and token[1] == "yazdır":
                line = int(_levels[i][1]) * "    " + "print" + "(" + token[2] + ")"

            parsed_lines.append(line)

        parsed_lines.append("\n")
        parsed_lines.append('if __name__ == "__main__":')
        parsed_lines.append('    Program.Main()')

        for p in parsed_lines:
            output_code = output_code + p + "\n"

        return output_code
