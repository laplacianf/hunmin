class emptyStatement:
    def __init__(self, indent, internalTokens):
        self.indent = indent
        self.internalTokens = internalTokens

        self.parsedCode = ''


class classStatement:
    def __init__(self, indent, name, inherit, internalTokens):
        self.indent = indent
        self.name = name
        self.inherit = inherit
        self.internalTokens = internalTokens
    


class varExprStatement:
    def __init__(self, indent, name, value):
        self.indent = indent
        self.name = name
        self.value = value
    
    def __repr__(self):
        return '{}{} = {}\n'.format(self.indent * '    ', self.name, self.value)
