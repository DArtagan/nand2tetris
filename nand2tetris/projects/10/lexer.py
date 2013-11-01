from token import Token

class Lexer:
    # Constants
    SYMBOLS = ['{' '}' '(' ')' '[' ']' '.' ',' ';' '+' 
               '-' '*' '/' '&' '|' '<' '>' '=' '~']
    KEYWORDS = ['class' 'constructor' 'function' 'method' 'field' 
                'static' 'var' 'int' 'char' 'boolean' 
                'void' 'true' 'false' 'null' 'this' 
                'let' 'do' 'if' 'else' 'while' 'return']

    tokens = [ ]

    def __init__(self, in_file):
        self.in_file = open(in_file, 'r') 
        c = self.in_file.read(1)
        self.file_pointer = self.in_file.tell()
        while True:
            # c = self.read()
            self.read()
            self.file_pointer = self.in_file.tell()
            if not c:
                break
            elif c == '/':
                self.comment()
                continue
            elif c.isdigit():
                integerConstant(c)
                continue
            elif c == '"':
                stringConstant(c)
                continue
            elif c in self.SYMBOLS:
                symbol(c)
                continue
            elif c.isalpha() | c == '_':
                identifier(c)
                continue

    def __str__(self):
        output = ""
        for token in self.tokens:
            output += str(token) + "\n"
        return output

    def read(self):
        self.in_file.seek(self.file_pointer)
        self.file_pointer += 1
        print(self.in_file.tell())
        return self.in_file.read(1)

    def add(self, flavour, value):
        self.tokens.append(Token(flavour, value))

    def comment(self):
        c = self.read()
        if c == '/':
            # while c != '\n':
            #     c = self.read()
            self.in_file.readline()
            self.file_pointer = self.in_file.tell()
#            print('hi')
        elif c == '*':
            while True:
                while c != '*':
                    c = self.read()
                c = self.read()
                if c == '/':
                    break
 #           print('Hello')
        else:
            self.symbol('/')
#            print('Yikes')
#        print(' there')

    def integerConstant(self, c):
        while c.isdigit():
            value += c
            c = self.read()
        self.add("stringConstant", value)

    def stringConstant(self):
        self.read()
        while c != '"':
            value += c
            c = self.read()
        self.add("stringConstant", value)
        self.read()

    def symbol(self, c):
        self.add("symbol", c)
        self.read()

    def identifier(self, c):
        output = c
        c = self.read()
        while c.isalpha() | c.isdigit() | c == '_':
            output += c
        if output in self.KEYWORDS:
            self.keyword(output)
        else:
            self.add("identifier", output)

    def keyword(self, keyword):
        self.add("keyword", keyword)

print(Lexer("Square/Main.jack"))
