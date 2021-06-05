from language.lexer import Lexer
from language.parse import parse
import config
from datetime import datetime

def compile(fileName):
    if fileName.split('.')[-1] != 'hmn': #hunmin 파일 일때만 실행
        raise BaseException('.{} 파일은 컴파일 할 수 없습니다'.format(fileName.split('.')[-1])) #hunmin 파일이 아니면 에러 반환
    
    #hunmin 헤더 추가
    hunminHeader = f'''######################################################
# 이 파일은 훈민 v{config.version} 으로 작성되었습니다
# 
# {datetime.today()}
######################################################\n
'''

    with open(fileName, 'r', encoding='UTF8') as File: hunminCode = ' '.join(''.join(File.readlines()).split('\n')) #줄바꿈 무시


    hunminLexer = Lexer(hunminCode)

    fileName = fileName.split('.')
    del fileName[-1] #.hmn 확장자 제거
    
    #확장자를 .py로 변경
    compiledPythonFileName = '.'.join(fileName) + '.py'

    with open(compiledPythonFileName, 'w', encoding='UTF8') as File: File.write(hunminHeader + parse(hunminLexer.lex(), 0))
