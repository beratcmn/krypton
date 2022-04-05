import 'TokenType.dart';

class Token {
  TokenType type;
  String lexeme;
  Object? literal;
  int line;

  String toString() {
    return type.toString() + " " + lexeme + " " + literal.toString();
  }

  Token(this.type, this.lexeme, this.literal, this.line);
}
