from language.lexer import Lexer
from language.parse import Parser


if __name__ == '__main__':
    code = '''
    사람수 는 3 이고
    
    사탕수수나무 은 사람수 더하기 3 나누기 2 임

    재윤의나이 는 15.7 + 3.14 임
    '''

    hunminLexer = Lexer(''.join(code.split('\n')))
    hunminParser = Parser()
    print(hunminLexer.lex())
    print(hunminParser.parse(hunminLexer.lex()))