import 'Token.dart';
import 'TokenType.dart';

class Scanner {
  String source;
  List<Token> tokens;
  int start = 0;
  int current = 0;
  int line = 1;

  Scanner(this.source, this.tokens);

  List<Token> scanTokens() {
    while (!isAtEnd()) {
      // We are at the beginning of the next lexeme.
      start = current;
      scanToken();
    }

    bool isAtEnd() {
      return current >= source.length();
    }

    tokens.add(new Token(EOF, "", null, line));
    return tokens;
  }

  void scanToken() {
    char c = advance();
    switch (c) {
      case '(':
        addToken(LEFT_PAREN);
        break;
      case ')':
        addToken(RIGHT_PAREN);
        break;
      case '{':
        addToken(LEFT_BRACE);
        break;
      case '}':
        addToken(RIGHT_BRACE);
        break;
      case ',':
        addToken(COMMA);
        break;
      case '.':
        addToken(DOT);
        break;
      case '-':
        addToken(MINUS);
        break;
      case '+':
        addToken(PLUS);
        break;
      case ';':
        addToken(SEMICOLON);
        break;
      case '*':
        addToken(STAR);
        break;
    }
  }
}
