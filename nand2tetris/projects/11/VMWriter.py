#============================================================
# PROGRAMMER:........ William H. Weiskopf
# USERID:............ WWEISKOP
# COURSE:............ CSCI-410
# TERM............... FALL 2013
# ASIGNMENT:......... ECS 10
# FILENAME:.......... VMWriter.py
# PYTHON VERSION:.... 3.3.0
#============================================================
import re

class VMWriter:
    statements = ['let', 'if', 'while', 'do', 'return']
    commands = {'+': 'add',
                '*': 'call Math.multiply',
                '/': 'call Math.divide',
               }

    def __init__(self, xml):
        self.vm = []
        self.pointer = 0
        self.prepend = ''

        self.xml = xml
        self.parser()
        for line in self.vm:
            print(str(line))

    def parser(self):
        while self.pointer < len(self.xml):
            if self.label() == 'class':
                self.parse_class()
            elif (self.label() == 'expressionList'):
                self.parse_expressionList()
            elif (self.label() == 'keyword') & (self.value() == 'return'):
                self.parse_return()
            self.pointer += 1

    def label(self, pointer=None):
        line = str(self.xml[pointer or self.pointer])
        label = re.search('<(\/?[a-zA-Z]+?)>', line).group(1)
        return label

    def value(self, pointer=None):
        line = str(self.xml[pointer or self.pointer])
        try:
            value = re.search('> (.+?) <', line).group(1)
        except:
            value = None
        return value
    
    def parse_class(self):
        self.pointer += 2
        self.prepend = self.value()
        self.pointer += 2

    def parse_expressionList(self):
        ex_list = []
        self.pointer += 1
        while self.label() != '/expressionList':
            if self.label() == 'expression':
                self.parse_expression()
            self.pointer += 1

    def parse_expression(self):
        ex_list = []
        self.pointer += 1
        while self.label() != '/expression':
            if self.label() == 'term':
                self.parse_term()
            elif (self.label() == 'symbol') & (self.value() in self.commands):
                self.vm.append(self.commands[self.value()])
            self.pointer += 1

    def parse_term(self):
        ex_list= []
        self.pointer += 1
        if self.label() == 'expression':
            self.parse_expression()
        elif self.label() == 'integerConstant':
            self.vm.append('push' + self.value())
            self.pointer += 1
        elif self.label() == '/term':
            return

    def parse_return(self):
        self.vm.append('return')

    def getVM(self):
        return self.vm
