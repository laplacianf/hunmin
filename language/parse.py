import language.errors as errors
from language.ast import functionStatement, varExprStatement, ifStatement, elifStatement, elseStatement, whileStatement, returnStatement, functionStatement


    
def parse(tokens, currentIndent):
    parseResult = ''
    currentPos = 0
    isString = False

    previousExpr = '' #현재 전까지의, 내부적으로 정의되지 않은 함수/클래스 처리
    internalExpr = [] #블럭 안에 구문
    tokenExpr = [] 

    while currentPos < len(tokens):
        currentToken = tokens[currentPos]

        if currentToken == '=': #변수 선언문 처리
            try:
                if currentPos - 1 >= 0:
                    varName = tokens[currentPos - 1]
                else:
                    raise errors.missingNameTypeError
            except IndexError:
                raise errors.missingNameTypeError
                
            currentPos += 1 #'=' 더하는것을 방지

            try:
                while True: #선언문 종료일때까지/문자열 안에 'EOS'가 아니면
                    if tokens[currentPos] == 'EOS' and not(isString):
                        break

                    if tokens[currentPos] == '"' and not(isString): #만약 '"'인데 문자열이 아니면 문자열을 시작
                        isString = True
                            
                    elif tokens[currentPos] == '"' and isString: #만약 '"'인데 문자열이면 문자열을 종료
                        isString = False

                    tokenExpr.append(tokens[currentPos])
                    currentPos += 1
                        
            except IndexError:
                raise errors.missingEOSError
                
            parseResult += str(varExprStatement(currentIndent, varName, ''.join(tokenExpr)))

            tokenExpr = [] #초기화
            
        elif currentToken == 'if':
            currentPos += 1 #'if'를 더하는것을 방지
            opened = 1 #특정 문이 겹처 있을때 종료 감지

            try:
                while True:
                    if tokens[currentPos] == 'then' and not(isString):
                        break

                    if tokens[currentPos] == '"' and not(isString): #만약 '"'인데 문자열이 아니면 문자열을 시작
                        isString = True
                            
                    elif tokens[currentPos] == '"' and isString: #만약 '"'인데 문자열이면 문자열을 종료
                        isString = False

                    tokenExpr.append(tokens[currentPos])
                    currentPos += 1

            except IndexError:
                raise errors.missingThenError
                
            currentPos += 1

            try:
                while True:
                    if tokens[currentPos] == 'END' and not(isString):
                        opened -= 1 #하나를 닫음

                    if (tokens[currentPos] == 'then' and not(isString)) or (tokens[currentPos] == 'while' and not(isString)) or (tokens[currentPos] == 'else' and not(isString)) or (tokens[currentPos] == 'def' and not(isString)):
                        opened += 1 #하나를 염
                    
                    if opened == 0: #만약 다 닫혔다면
                        break

                    if tokens[currentPos] == '"' and not(isString): #만약 '"'인데 문자열이 아니면 문자열을 시작
                        isString = True
                            
                    elif tokens[currentPos] == '"' and isString: #만약 '"'인데 문자열이면 문자열을 종료
                        isString = False

                    internalExpr.append(tokens[currentPos])
                    currentPos += 1
                
            except IndexError:
                raise errors.missingEndError
            
       
            parseResult += str(ifStatement(currentIndent, ''.join(tokenExpr), parse(internalExpr, currentIndent + 1)))

            tokenExpr = []
            internalExpr = [] #초기화

        elif currentToken == 'elif':
            currentPos += 1 #'elif'를 더하는것을 방지
            opened = 1 #특정 문이 겹처 있을때 종료 감지

            try:
                while True:
                    if tokens[currentPos] == 'then' and not(isString):
                        break

                    if tokens[currentPos] == '"' and not(isString): #만약 '"'인데 문자열이 아니면 문자열을 시작
                        isString = True
                            
                    elif tokens[currentPos] == '"' and isString: #만약 '"'인데 문자열이면 문자열을 종료
                        isString = False

                    tokenExpr.append(tokens[currentPos])
                    currentPos += 1

            except IndexError:
                raise errors.missingThenError
                
            currentPos += 1

            try:
                while True:
                    if tokens[currentPos] == 'END' and not(isString):
                        opened -= 1 #하나를 닫음

                    if (tokens[currentPos] == 'then' and not(isString)) or (tokens[currentPos] == 'while' and not(isString)) or (tokens[currentPos] == 'else' and not(isString)) or (tokens[currentPos] == 'def' and not(isString)):
                        opened += 1 #하나를 염
                    
                    if opened == 0: #만약 다 닫혔다면
                        break

                    if tokens[currentPos] == '"' and not(isString): #만약 '"'인데 문자열이 아니면 문자열을 시작
                        isString = True
                            
                    elif tokens[currentPos] == '"' and isString: #만약 '"'인데 문자열이면 문자열을 종료
                        isString = False

                    internalExpr.append(tokens[currentPos])
                    currentPos += 1
                
            except IndexError:
                raise errors.missingEndError
            
       
            parseResult += str(elifStatement(currentIndent, ''.join(tokenExpr), parse(internalExpr, currentIndent + 1)))

            tokenExpr = []
            internalExpr = [] #초기화
        
        elif currentToken == 'else':
            currentPos += 1
            opened = 1 #특정 문이 겹쳐있는지 확인

            try:
                while True:
                    if tokens[currentPos] == 'END' and not(isString):
                        opened -= 1 #하나를 닫음

                    if (tokens[currentPos] == 'then' and not(isString)) or (tokens[currentPos] == 'while' and not(isString)) or (tokens[currentPos] == 'else' and not(isString)) or (tokens[currentPos] == 'def' and not(isString)):
                        opened += 1 #하나를 염
                    
                    if opened == 0: #만약 다 닫혔다면
                        break

                    if tokens[currentPos] == '"' and not(isString): #만약 '"'인데 문자열이 아니면 문자열을 시작
                        isString = True
                            
                    elif tokens[currentPos] == '"' and isString: #만약 '"'인데 문자열이면 문자열을 종료
                        isString = False

                    internalExpr.append(tokens[currentPos])
                    currentPos += 1
                
            except IndexError:
                raise errors.missingEndError

            parseResult += str(elseStatement(currentIndent, parse(internalExpr, currentIndent + 1)))

            tokenExpr = []
            internalExpr = [] #초기화
        
        elif currentToken == 'while':
            currentPos += 1
            opened = 1 #특정 문이 겹쳐있는지 확인

            try:
                while True:
                    if tokens[currentPos] == 'END' and not(isString):
                        opened -= 1 #하나를 닫음

                    if (tokens[currentPos] == 'then' and not(isString)) or (tokens[currentPos] == 'while' and not(isString)) or (tokens[currentPos] == 'else' and not(isString)) or (tokens[currentPos] == 'def' and not(isString)):
                        opened += 1 #하나를 염
                    
                    if opened == 0: #만약 다 닫혔다면
                        break

                    if tokens[currentPos] == '"' and not(isString): #만약 '"'인데 문자열이 아니면 문자열을 시작
                        isString = True
                            
                    elif tokens[currentPos] == '"' and isString: #만약 '"'인데 문자열이면 문자열을 종료
                        isString = False

                    internalExpr.append(tokens[currentPos])
                    currentPos += 1
                
            except IndexError:
                raise errors.missingEndError

            parseResult += str(whileStatement(currentIndent, previousExpr, parse(internalExpr, currentIndent + 1)))

            previousExpr = '' #초기화
        
        elif currentToken == 'break':
            parseResult += '\n{}break\n'.format(currentIndent * '    ')

        
        elif currentToken == 'CALL': #함수 실행
            parseResult += currentIndent * '    ' + previousExpr + '\n' #현재 전까지의 내용을 더함

            previousExpr = '' #초기화
        
        elif currentToken == 'return':
            currentPos += 1 #'return'을 더하는것을 방지

            try:
                while True:
                    if tokens[currentPos] == 'EOR' and not(isString):
                        break

                    if tokens[currentPos] == '"' and not(isString): #만약 '"'인데 문자열이 아니면 문자열을 시작
                        isString = True
                            
                    elif tokens[currentPos] == '"' and isString: #만약 '"'인데 문자열이면 문자열을 종료
                        isString = False
                    
                    tokenExpr.append(tokens[currentPos])
                    currentPos += 1
            
            except IndexError:
                raise errors.missingEORError
            
            parseResult += str(returnStatement(currentIndent, ''.join(tokenExpr)))

            tokenExpr = [] #초기화

        
        elif currentToken == 'for':
            pass

        elif currentToken == 'def':
            currentPos += 1
            opened = 1 #특정 문이 겹쳐있는지 확인

            functionName = '' #함수의 이름

            try:
                while True:
                    if tokens[currentPos] == '=' and not(isString):
                            break

                    if tokens[currentPos] == '"' and not(isString): #만약 '"'인데 문자열이 아니면 문자열을 시작
                        isString = True
                                
                    elif tokens[currentPos] == '"' and isString: #만약 '"'인데 문자열이면 문자열을 종료
                        isString = False
                    
                    functionName += tokens[currentPos]
                    currentPos += 1
                
            except IndexError:
                raise errors.missingEqualError
            
            currentPos += 1 #'=' 더하는 것을 방지
            
            try:
                while True:
                    if tokens[currentPos] == 'END' and not(isString):
                        opened -= 1 #하나를 닫음

                    if (tokens[currentPos] == 'then' and not(isString)) or (tokens[currentPos] == 'while' and not(isString)) or (tokens[currentPos] == 'else' and not(isString)) or (tokens[currentPos] == 'def' and not(isString)):
                        opened += 1 #하나를 염
                    
                    if opened == 0: #만약 다 닫혔다면
                        break

                    if tokens[currentPos] == '"' and not(isString): #만약 '"'인데 문자열이 아니면 문자열을 시작
                        isString = True
                            
                    elif tokens[currentPos] == '"' and isString: #만약 '"'인데 문자열이면 문자열을 종료
                        isString = False

                    internalExpr.append(tokens[currentPos])
                    currentPos += 1
                
            except IndexError:
                raise errors.missingEndError
            
            parseResult += str(functionStatement(currentIndent, functionName, parse(internalExpr, currentIndent + 1)))
            
            internalExpr = [] #초기화

        else:
            try:
                if tokens[currentPos + 1] != '=': #변수 이름을 더하는 것을 방지
                    previousExpr += currentToken #내용에 현재 토큰 더하기
            
            except IndexError:
                previousExpr += currentToken #만약 코드의 마지막 문자라면

        
        
        currentPos += 1
    
    return parseResult
