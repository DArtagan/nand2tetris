#============================================================
# PROGRAMMER:........ William H. Weiskopf
# USERID:............ WWEISKOP
# COURSE:............ CSCI-410
# TERM............... FALL 2013
# ASIGNMENT:......... ECS 10
# FILENAME:.......... tokenizer.py
# PYTHON VERSION:.... 3.3.0
#============================================================
from token import JackToken

class JackTokenizer:

    # Constants
    SYMBOLS = ['{', '}', '(', ')', '[', ']', '.', ',', ';', '+', 
               '-', '*', '/', '&', '|', '<', '>', '=', '~']
    KEYWORDS = ['class', 'constructor', 'function', 'method', 'field',
                'static', 'var', 'int', 'char', 'boolean',
                'void', 'true', 'false', 'null', 'this',
                'let', 'do', 'if', 'else', 'while', 'return']

    # Varibles
    jack_tokens = [ ]

    # Methods
    def __init__(self, in_file):
        self.in_file = open(in_file, 'r') 
        c = self.read()
        while True:
            if not c:
                break
            elif c == '/':
                c = self.comment()
                continue
            elif c.isdigit():
                c = self.integerConstant(c)
                continue
            elif c == '"':
                c = self.stringConstant(c)
                continue
            elif c in self.SYMBOLS:
                self.symbol(c)
                c = self.read()
                continue
            elif (c.isalpha()) | (c == '_'):
                c = self.identifier(c)
                continue
            else:
                c = self.read()

    def __str__(self):
        output = "<tokens>"
        for token in self.jack_tokens:
            output += str(token) + "\n"
        output += "</tokens>"
        return output

    def read(self):
        return self.in_file.read(1)

    def add(self, flavour, value):
        self.jack_tokens.append(JackToken(flavour, value))

    def write(self, out_file):
        out = open(out_file, 'w')
        for token in self.jack_tokens:
            out.write(str(token) + '\n')

    def comment(self):
        c = self.read()
        if c == '/':
            self.in_file.readline()
            self.read()
        elif c == '*':
            self.read()
            while True:
                while c != '*':
                    c = self.read()
                c = self.read()
                if c == '/':
                    break
            c = self.read()
        else:
            self.symbol('/')
        return c

    def integerConstant(self, c):
        value = ""
        while c.isdigit():
            value += c
            c = self.read()
        if(int(value) > 32767):
            print("Overly large integer.")
        self.add("stringConstant", value)
        return c

    def stringConstant(self):
        self.read()
        while c != '"':
            value += c
            c = self.read()
        self.add("stringConstant", value)
        return c

    def symbol(self, c):
        self.add("symbol", c)

    def identifier(self, c):
        output = c
        c = self.read()
        while (c.isalpha()) | (c.isdigit()) | (c == '_'):
            output += c
            c = self.read()
        if output in self.KEYWORDS:
            self.keyword(output)
        else:
            self.add("identifier", output)
        return c

    def keyword(self, keyword):
        self.add("keyword", keyword)

    def getJackTokens(self):
        return self.jack_tokens
