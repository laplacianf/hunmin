from language.lexer import Lexer
from language.parse import parse


if __name__ == '__main__':
    code = '''
변수 는 3 이고 나 는 7 임

만약 변수 가 4 이면
    변수 는 5 임
    
    사람수 는 1 + 5/3.141592 이고
    변수는 사람수 더하기 3

    만약 사람수 가 4 나누기 3 이면
        변수 는 78 임
        
        만약 변수 가 78 이면
            변수 는 89 임
        
        를 함
    
    을 함

를 함

만약 나 가 7 이면
    변수 는 89 임

을 함
'''

    hunminLexer = Lexer(' '.join(code.split('\n')))
    print(hunminLexer.lex())
    print(parse(hunminLexer.lex(), 0))

