import 'Token.dart';
import 'TokenType.dart';
import 'Krypton.dart';

class Scanner {
  final String source;
  final List<Token> tokens = [];
  int start = 0;
  int current = 0;
  int line = 1;

  Scanner(this.source);

  List<Token> scanTokens() {
    while (!isAtEnd()) {
      // We are at the beginning of the next lexeme.
      start = current;
      scanToken();
    }

    tokens.add(new Token(TokenType.EOF, "", null, line));
    return tokens;
  }

  bool isAtEnd() {
    return current >= source.length;
  }

  void scanToken() {
    var c = advance();
    switch (c) {
      case '(':
        addToken(TokenType.LEFT_PAREN);
        break;
      case ')':
        addToken(TokenType.RIGHT_PAREN);
        break;
      case '{':
        addToken(TokenType.LEFT_BRACE);
        break;
      case '}':
        addToken(TokenType.RIGHT_BRACE);
        break;
      case ',':
        addToken(TokenType.COMMA);
        break;
      case '.':
        addToken(TokenType.DOT);
        break;
      case '-':
        addToken(TokenType.MINUS);
        break;
      case '+':
        addToken(TokenType.PLUS);
        break;
      case ';':
        addToken(TokenType.SEMICOLON);
        break;
      case '*':
        addToken(TokenType.STAR);
        break;
      case '!':
        addToken(match('=') ? TokenType.BANG_EQUAL : TokenType.BANG);
        break;
      case '=':
        addToken(match('=') ? TokenType.EQUAL_EQUAL : TokenType.EQUAL);
        break;
      case '<':
        addToken(match('=') ? TokenType.LESS_EQUAL : TokenType.LESS);
        break;
      case '>':
        addToken(match('=') ? TokenType.GREATER_EQUAL : TokenType.GREATER);
        break;
      case '/':
        if (match('/')) {
          // A comment goes until the end of the line.
          while (peek() != '\n' && !isAtEnd()) advance();
        } else {
          addToken(TokenType.SLASH);
        }
        break;
      case ' ':
      case '\r':
      case '\t':
        // Ignore whitespace.
        break;

      case '\n':
        line++;
        break;
      case '"':
        string();
        break;
      default:
        if (isDigit(c)) {
          number();
        } else if (isAlpha(c)) {
          identifier();
        } else {
          error(line, "Unexpected character.");
        }
        break;
    }
  }

  String advance() {
    return source[current++];
  }

  bool match(String expected) {
    if (isAtEnd()) return false;
    if (source[current] != expected) return false;

    current++;
    return true;
  }

  bool isDigit(String c) {
    var u = c.codeUnitAt(0);
    return u >= 48 && u <= 57;
  }

  bool isAlpha(String c) {
    var u = c.codeUnitAt(0);
    return (u >= 97 && u <= 122) || (u >= 65 && u <= 90) || c == '_';
  }

  bool isAlphaNumeric(String c) {
    return isAlpha(c) || isDigit(c);
  }

  String peek() {
    if (isAtEnd()) return '\x00';
    return source[current];
  }

  String peekNext() {
    if (current + 1 >= source.length) return '\x00';
    return source[current + 1];
  }

  void addToken(TokenType type, [Object? literal]) {
    var text = source.substring(start, current);
    tokens.add(Token(type, text, literal, line));
  }

  void addToken_(TokenType type, Object? literal) {
    String text = source.substring(start, current);
    tokens.add(new Token(type, text, literal, line));
  }

  void string() {
    while (peek() != '"' && !isAtEnd()) {
      if (peek() == '\n') line++;
      advance();
    }

    if (isAtEnd()) {
      error(line, "Unterminated string.");
      return;
    }

    // The closing ".
    advance();

    // Trim the surrounding quotes.
    String value = source.substring(start + 1, current - 1);
    addToken(TokenType.STRING, value);
  }

  void number() {
    while (isDigit(peek())) advance();

    // Look for a fractional part.
    if (peek() == '.' && isDigit(peekNext())) {
      // Consume the "."
      advance();

      while (isDigit(peek())) advance();
    }

    addToken(TokenType.NUMBER, double.parse(source.substring(start, current)));
  }

  void identifier() {
    while (isAlphaNumeric(peek())) advance();

    String text = source.substring(start, current);
    TokenType type = keywords.get(text);
    if (type == null) type = TokenType.IDENTIFIER;
    addToken(type);
  }

  static const keywords = <String, TokenType>{
    've': TokenType.AND,
    'sınıf': TokenType.CLASS,
    'değilse': TokenType.ELSE,
    'yanlış': TokenType.FALSE,
    'for': TokenType.FOR,
    'fonksiyon': TokenType.FUN,
    'eğer': TokenType.IF,
    'yok': TokenType.NIL,
    'veya': TokenType.OR,
    'yazdır': TokenType.PRINT,
    'döndür': TokenType.RETURN,
    'super': TokenType.SUPER,
    'this': TokenType.THIS,
    'doğru': TokenType.TRUE,
    'değişken': TokenType.VAR,
    'süresince': TokenType.WHILE,
  };
}
