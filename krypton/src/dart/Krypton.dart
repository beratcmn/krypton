import 'Token.dart';
import 'TokenType.dart';

import 'dart:io';

bool hadError = false;

void main(List<String> args) {
  if (args.length > 1) {
    print("Kullanım: krypton [dosya_adı]");
    exit(0);
  } else if (args.length == 1) {
    // runFile(args[0]);
  } else {
    // runPrompt();
  }
}

void run(String source) {
  // Scanner = new Scanner(source);
  List<Token> tokens = scanner.ScanTokens();

  for (Token token in tokens) {
    print(token);
  }
}

void runFile(String path) {
  if (hadError) {
    exit(0);
  }
}

void error(int line, String message) {
  report(line, "", message);
}

void report(int line, String where, String message) {
  print("[line " + line.toString() + "] Error" + where + ": " + message);
  hadError = true;
}
