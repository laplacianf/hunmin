class Lexer:
    def __init__(self, code):
        self.currentPos = 0
        self.word = ''

        self.lexResult = []

        self.code = code + ' ' #마지막 토큰 처리
    def advance(self):
        self.currentPos += 1
    
    def returnCurrentChar(self):
        return self.code[self.currentPos]
    
    def returnCharAt(self, pos):
        return self.code[pos]
    
    def lex(self):
        while self.currentPos < len(self.code):
            currentChar = self.returnCurrentChar()

            if currentChar == ' ':
                if self.word == '은' or self.word == '는': self.lexResult.append('IS')
                elif self.word == '임': self.lexResult.append('EOS')
                elif self.word == '이고': self.lexResult.append('EOS')
                elif self.word == '함' or self.word == '하고': self.lexResult.append('END')
                elif self.word == '이면' or self.word == '라면': self.lexResult.append('THEN')
                elif self.word == '인': self.lexResult.append('WHILE')
                elif self.word == '만약': self.lexResult.append('IF')
                elif self.word == '아니면': self.lexResult.append('ELSE')
                elif self.word == '아니고': self.lexResult.append('ELIF')
                elif self.word == '함수': self.lexResult.append('FUNCTION')
                elif self.word == '다음': self.lexResult.append('RETURN')
                elif self.word == '반환': self.lexResult.append('EOR')
                elif self.word == '을' or self.word == '를': pass

                elif self.word == '더하기': self.lexResult.append('+')
                elif self.word == '빼기': self.lexResult.append('-')
                elif self.word == '곱하기': self.lexResult.append('*')
                elif self.word == '나누기': self.lexResult.append('/')

                elif self.word == '이상': self.lexResult.append('>=')
                elif self.word == '초과': self.lexResult.append('>')
                elif self.word == '이하': self.lexResult.append('<=')
                elif self.word == '미만': self.lexResult.append('<')

                elif self.word == '제곱': self.lexResult.append('**')
                elif self.word == '나눈나머지': self.lexResult.append('%')
                elif self.word == '나눈몫': self.lexResult.append('//')

                elif self.word == '가' or self.word == '이': self.lexResult.append('==')
                elif self.word == '가아님' or self.word == '이아님': self.lexResult.append('!=')

                elif self.word == '그리고': self.lexResult.append('AND')
                elif self.word == '또는': self.lexResult.append('OR')

                elif self.word == '참': self.lexResult.append('True')
                elif self.word == '거짓': self.lexResult.append('False')




                elif self.word != '': self.lexResult.append(self.word)
                self.word = ''
            
            else: self.word += currentChar

            self.advance()
        
        return self.lexResult


code = '''
함수 소수인지판별(숫자) 은 만약 숫자 가 1 이면 다음 거짓 을 반환 하고 아니면 나눔 은 2 이고 나눔 미만 숫자 인 동안 만약 숫자 나눗셈 나머지 가 0 이면 다음 거짓 을 반환 함 나눔 은 나눔 더하기 1 임을 하고 다음 참 을 반환 을 함 

'''
            
L = Lexer(''.join(code.split('\n')))
print(L.lex())
