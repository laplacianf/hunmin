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
                elif self.word == '임': self.lexResult.append('END')
                elif self.word == '이고': self.lexResult.append('EOS')
                elif self.word == '함': self.lexResult.append('END')
                elif self.word == '이면' or self.word == '라면': self.lexResult.append('THEN')
                elif self.word == '인': self.lexResult.append('WHILE')
                elif self.word == '만약': self.lexResult.append('IF')
                elif self.word == '아니면': self.lexResult.append('ELSE')
                elif self.word == '아니고': self.lexResult.append('ELIF')
                elif self.word == '함수': self.lexResult.append('FUNCTION')
                elif self.word == '을' or self.word == '를': pass

                elif self.word == '더하기': self.lexResult.append('+')
                elif self.word == '빼기': self.lexResult.append('-')
                elif self.word == '곱하기': self.lexResult.append('*')
                elif self.word == '나누기': self.lexResult.append('/')

                elif self.word == '제곱': self.lexResult.append('**')
                elif self.word == '나눈나머지': self.lexResult.append('%')
                elif self.word == '나눈몫': self.lexResult.append('//')

                elif self.word == '가' or self.word == '이': self.lexResult.append('==')
                elif self.word == '가아님' or self.word == '이아님': self.lexResult.append('!=')

                elif self.word == '그리고': self.lexResult.append('AND')
                elif self.word == '또는': self.lexResult.append('OR')




                elif self.word != '': self.lexResult.append(self.word)
                self.word = ''
            
            else: self.word += currentChar

            self.advance()
        
        return self.lexResult


code = '''
함수 아무거나(숫자) 는 
    만약 숫자 가 3 또는 숫자 더하기 5 빼기 6 곱하기 7 이 8 이면 
        숫자 는 1 임
    을 함
    아니면 
        숫자 는 2 임 
    을 함
를 함 


함수 제곱(숫자) 는
    숫자 는 숫자 곱하기 숫자 

를 함 

가 는 5 임 
나 는 6 이고 다 는 나 더하기 6 임
'''
            
L = Lexer(''.join(code.split('\n')))
print(L.lex())