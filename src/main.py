from language.lexer import Lexer
from language.parse import Parser


if __name__ == '__main__':
    code = '''
변수 는 ["EOS 는 1", 3.14, "안녕, 세상!"] 이고
나 는 3.141575 더하기 변수 임
'''

    hunminLexer = Lexer(' '.join(code.split('\n')))
    hunminParser = Parser()
    print(hunminLexer.lex())
    print(hunminParser.parse(hunminLexer.lex()))