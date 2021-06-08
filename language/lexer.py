class Lexer:
    def __init__(self, code):
        self.currentPos = 0
        self.word = ''

        self.lexResult = []

        self.code = code + ' ' #마지막 토큰 처리

        self.isString = False #문자열 처리
    def advance(self):
        self.currentPos += 1
    
    def returnCurrentChar(self):
        return self.code[self.currentPos]
    
    def returnCharAt(self, pos):
        return self.code[pos]
    
    def checkKeywords(self):
        if self.word == '은' or self.word == '는': self.lexResult.append('=') #변수 선언문
        elif self.word == '임': self.lexResult.append('EOS') #변수 선언문의 종료
        elif self.word == '이고': self.lexResult.append('EOS') #임과 동일
        elif self.word == '함' or self.word == '하고': self.lexResult.append('END') #:가 포함된 문의 종료
        elif self.word == '이면' or self.word == '라면': self.lexResult.append('then') #:가 포함된 문의 시작
        elif self.word == '동안': self.lexResult.append('while') #while문
        elif self.word == '종료': self.lexResult.append('break') #break문
        elif self.word == '만약': self.lexResult.append('if') #if문
        elif self.word == '아니면': self.lexResult.append('else') #else문
        elif self.word == '아니고': self.lexResult.append('elif') #elif문
        elif self.word == '함수': self.lexResult.append('def') #def문
        elif self.word == '값': self.lexResult.append('return') #return문
        elif self.word == '반환함' or self.word == '반환하고': self.lexResult.append('EOR') #return문 종료
        elif self.word == '실행함' or self.word == '실행하고': self.lexResult.append('CALL') #함수를 실행
        elif self.word == '을' or self.word == '를' or self.word == '인': pass #자연스러운 처리를 위함

        #클래스 처리
        elif self.word == '의' or self.word == '에': self.lexResult.append('.')

        #연산자 처리
        elif self.word == '더하기': self.lexResult.append('+') 
        elif self.word == '빼기': self.lexResult.append('-')
        elif self.word == '곱하기': self.lexResult.append('*')
        elif self.word == '나누기': self.lexResult.append('/')

        #부등호 처리
        elif self.word == '이상': self.lexResult.append('>=')
        elif self.word == '초과': self.lexResult.append('>')
        elif self.word == '이하': self.lexResult.append('<=')
        elif self.word == '미만': self.lexResult.append('<')

        #특수 연산자 처리
        elif self.word == '제곱': self.lexResult.append('**')
        elif self.word == '나눈나머지': self.lexResult.append('%')
        elif self.word == '나눈몫': self.lexResult.append('//')

        #같음/같지 않음 처리
        elif self.word == '가' or self.word == '이': self.lexResult.append('==')
        elif self.word == '가아님' or self.word == '이아님': self.lexResult.append('!=')

        #논리 연산자 처리
        elif self.word == '그리고': self.lexResult.append(' and ')
        elif self.word == '또는': self.lexResult.append(' or ')

        #bool 처리
        elif self.word == '참': self.lexResult.append('True')
        elif self.word == '거짓': self.lexResult.append('False')

        #자료형 클래스 처리
        elif self.word == '정수': self.lexResult.append('int')
        elif self.word == '실수': self.lexResult.append('float')
        elif self.word == '문자열': self.lexResult.append('str')
        elif self.word == '불': self.lexResult.append('bool')
        elif self.word == '배열': self.lexResult.append('list')
        elif self.word == '집합': self.lexResult.append('set')
        elif self.word == '사전': self.lexResult.append('dict')
        elif self.word == '묶음': self.lexResult.append('tuple')

        #내장함수 처리
        elif self.word == '출력': self.lexResult.append('print')
        elif self.word == '입력받기': self.lexResult.append('input')
        elif self.word == '추가': self.lexResult.append('append')

        elif self.word != '': self.lexResult.append(self.word)
        self.word = ''
                
    
    def lex(self):
        while self.currentPos < len(self.code):
            currentChar = self.returnCurrentChar()
            if not(self.isString):
                if currentChar == ' ':
                    self.checkKeywords()
                    
                elif currentChar == '"': #문자열의 시작이라면
                    self.lexResult.append('"')
                    self.isString = True
                
                elif currentChar == '(': #함수, 오브젝트 처리
                    self.checkKeywords()

                    self.lexResult.append('(')
                
                elif currentChar == ')':
                    self.checkKeywords()
                    
                    self.lexResult.append(')')
                
                elif currentChar == '[': #배열 처리
                    self.checkKeywords()

                    self.lexResult.append('[')

                elif currentChar == ']':
                    self.checkKeywords()
                    
                    self.lexResult.append(']')
                
                elif currentChar == ',':
                    self.checkKeywords()
                    
                    self.lexResult.append(',')
            
                else: self.word += currentChar
            
            else:
                if currentChar == '"': #문자열의 끝이라면
                    self.lexResult.append(self.word)
                    self.lexResult.append('"')
                    
                    self.word = ''

                    self.isString = False
                else: self.word += currentChar

            self.advance()
        
        return self.lexResult



            
