#============================================================
# PROGRAMMER:........ William H. Weiskopf
# USERID:............ WWEISKOP
# COURSE:............ CSCI-410
# TERM............... FALL 2013
# ASIGNMENT:......... ECS 10
# FILENAME:.......... compilation_engine.py
# PYTHON VERSION:.... 3.3.0
#============================================================
from token import JackToken

class Grammarizer:
    statements = ['let', 'if', 'while', 'do', 'return']

    def __init__(self, jack_tokens):
        self.xml = []
        self.pointer = 0
        self.jack_tokens = jack_tokens
        self.parser()
        # for item in self.xml:
        #     print(str(item))

    def write(self, out_file):
        out = open(out_file, 'w')
        for jack_token in self.xml:
            out.write(str(jack_token) + '\n')

    def parser(self):
        if self.jack_tokens[self.pointer] == JackToken('keyword', 'class'):
            self.compile_class()
        
    def check_token(self, flavour, values):
        if isinstance(values, list):
            print('True')
            print(str(self.pointer))
            for value in values:
                if self.jack_tokens[self.pointer] == JackToken(flavour, value):
                    return True
        else:
            if self.jack_tokens[self.pointer] == JackToken(flavour, values):
                return True
        return False

    def append_tokens(self, num):
        for i in range(0, num):
            self.xml.append(self.jack_tokens[self.pointer])
            self.pointer += 1

    def compile_class(self):
        self.xml.append('<class>')
        self.append_tokens(3)
        while (self.check_token('keyword', 'static')) | (self.check_token('keyword', 'field')):
            self.compile_classVarDec()
        while (self.check_token('keyword', 'constructor')) | (self.check_token('keyword', 'function')) | (self.check_token('keyword', 'method')):
            self.compile_subroutine()            
        self.append_tokens(1)
        self.xml.append('</class>')

    def compile_classVarDec(self):
        self.xml.append('<classVarDec>')
        self.append_tokens(2)
        test = True
        while test:
            self.append_tokens(1)
            self.xml.append(self.jack_tokens[self.pointer])
            if self.check_token('symbol', ';'):
                test = False
            self.pointer += 1
        self.xml.append('</classVarDec>')

    def compile_subroutine(self):
        self.xml.append('<subroutineDec>')
        self.append_tokens(4)
        self.compile_parameterList()
        self.append_tokens(1)
        self.xml.append('<subroutineBody>')
        self.append_tokens(1)
        while self.check_token('keyword', 'var'):
            self.compile_varDec()
        print(str(self.jack_tokens[self.pointer]))
        print(str(self.pointer) + ',' + str(len(self.jack_tokens)))
        self.xml.append('<statements>')
        while self.check_token('keyword', self.statements):
            print('>' + str(self.pointer))
            self.compile_statements()
        self.xml.append('</statements>')
        self.append_tokens(1)
        self.xml.append('</subroutineBody>')
        self.xml.append('</subroutineDec>')

    def compile_parameterList(self):
        self.xml.append('<parameterList>')
        while not self.check_token('symbol', ')'):
            self.append_tokens(2)
            if self.check_token('symbol', ','):
                self.append_tokens(1)
        self.xml.append('</parameterList>')

    def compile_varDec(self):
        self.xml.append('<varDec>')
        self.append_tokens(2)
        test = True
        while test:
            self.append_tokens(1)
            self.xml.append(self.jack_tokens[self.pointer])
            if self.check_token('symbol', ';'):
                test = False
            self.pointer += 1
        self.xml.append('</varDec>')

    def compile_statements(self):
        if self.check_token('keyword', 'let'):
            self.compile_let()
        elif self.check_token('keyword', 'if'):
            self.compile_if()
        elif self.check_token('keyword', 'while'):
            self.compile_while()
        elif self.check_token('keyword', 'do'):
            self.compile_do()
        elif self.check_token('keyword', 'return'):
            self.compile_return()

    def compile_let(self):
        self.xml.append('<letStatement>')
        self.append_tokens(2)
        if self.check_token('symbol', '['):
            self.append_tokens(1)
            self.compile_expression()
            self.append_tokens(1)
        self.append_tokens(1)
        self.compile_expression()
        self.append_tokens(1)
        self.xml.append('</letStatement>')

    def compile_if(self):
        self.xml.append('<ifStatement>')
        self.append_tokens(2)
        self.compile_expression()
        self.append_tokens(2)
        while self.check_token('keyword', self.statements):
            self.compile_statements()
        self.append_tokens(1)
        if self.check_token('keyword', 'else'):
            self.append_tokens(2)
            while self.check_token('keyword', self.statements):
                self.compile_statements()
            self.append_tokens(1)
        self.xml.append('</ifStatement>')

    def compile_while(self):
        self.xml.append('<whileStatement>')
        self.append_tokens(2)
        self.compile_expression()
        self.append_tokens(2)
        while self.check_token('keyword', self.statements):
            self.compile_statements()
        self.append_tokens(1)
        self.xml.append('</whileStatement>')

    def compile_do(self):
        self.xml.append('<doStatement>')
        self.append_tokens(1)
        self.compile_subroutineCall()
        self.append_tokens(1)
        self.xml.append('</doStatement>')

    def compile_return(self):
        self.xml.append('<returnStatement>')
        self.append_tokens(1)
        if not self.check_token('symbol', ';'):
            self.compile_expression()
        self.append_tokens(1)
        self.xml.append('</returnStatement>')

    def compile_subroutineCall(self):
        self.append_tokens(1)
        if self.check_token('symbol', '['):
            self.append_tokens(1)
            self.expression_list()
            self.append_tokens(1)
        if self.check_token('symbol', '.'):
            self.append_tokens(2)
        if self.check_token('symbol', '('):
            self.append_tokens(1)
            self.compile_expressionList()
            self.append_tokens(1)

    def compile_expression(self):
        self.xml.append('<expression>')
        self.compile_term()
        self.xml.append('</expression>')

    def compile_term(self):
        self.xml.append('<term>')
        self.append_tokens(1)
        self.xml.append('</term>')

    def compile_expressionList(self):
        self.xml.append('<expressionList>')
        while not self.check_token('symbol', ')'):
            self.compile_expression()
            if self.check_token('symbol', ','):
                self.append_tokens(1)
        self.xml.append('</expressionList>')

    def getXML(self):
        return self.xml
