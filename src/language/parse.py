import language.ast as ast, language.errors as errors
from language.ast import varExprStatement


class Parser:
    def __init__(self):
        self.globalNode = ast.emptyStatement(0, None)
        self.currentIndent = 0
    
    def parse(self, tokens):
        currentPos = 0
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
                
                currentPos += 1 #'='를 더하는것을 방지
                
                try:
                    while tokens[currentPos] != 'EOS': #선언문 종료일때까지
                        tokenExpr.append(tokens[currentPos])
                        currentPos += 1
                except IndexError:
                    raise errors.missingEOSError
                
                self.globalNode.parsedCode += str(varExprStatement(self.currentIndent, varName, ''.join(tokenExpr)))

                tokenExpr = [] #초기화
            else:
                pass

            currentPos += 1
        return self.globalNode.parsedCode
