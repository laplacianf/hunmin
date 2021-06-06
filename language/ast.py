class classStatement:
    def __init__(self, indent, name, inherit):
        self.indent = indent
        self.name = name
        self.inherit = inherit

        self.parsedCode = ''
    


class varExprStatement:
    def __init__(self, indent, name, value):
        self.indent = indent
        self.name = name
        self.value = value
    
    def __repr__(self):
        return '\n{}{} = {}\n'.format(self.indent * '    ', self.name, self.value)


class ifStatement:
    def __init__(self, indent, expr, parsedCode):
        self.indent = indent
        self.expr = expr

        self.parsedCode = parsedCode
    
    def __repr__(self):
        return '\n{}if {}:\n{}\n'.format(self.indent * '    ', self.expr, self.parsedCode)


class elifStatement:
    def __init__(self, indent, expr, parsedCode):
        self.indent = indent
        self.expr = expr

        self.parsedCode = parsedCode
    
    def __repr__(self):
        return '\n{}elif {}:\n{}\n'.format(self.indent * '    ', self.expr, self.parsedCode)


class elseStatement:
    def __init__(self, indent, parsedCode):
        self.indent = indent

        self.parsedCode = parsedCode
    
    def __repr__(self):
        return '\n{}else:\n{}\n'.format(self.indent * '    ', self.parsedCode)


class returnStatement:
    def __init__(self, indent, expr):
        self.indent = indent
        self.expr = expr
    
    def __repr__(self):
        return '\n{}return {}\n'.format(self.indent * '    ', self.expr)
