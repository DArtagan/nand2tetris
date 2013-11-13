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
       self.xml = xml
       self.parser()
       for line in self.vm:
           print(str(line))

    def parser(self):
        pointer = 0
        while pointer < len(self.xml):
            if (self.label(pointer) == 'expressionList'):
                pointer = self.parse_expressionList(pointer)
            elif (self.label(pointer) == 'keyword') & (self.value(pointer) == 'return'):
                pointer = self.parse_return(pointer)
            pointer += 1

    def label(self, pointer=self.pointer):
        line = str(self.xml[pointer])
        label = re.search('<(\/?[a-zA-Z]+?)>', line).group(1)
        return label

    def value(self, pointer=self.pointer):
        line = str(self.xml[pointer])
        try:
            value = re.search('> (.+?) <', line).group(1)
        except:
            value = None
        return value

    def parse_expressionList(self):
        self.pointer += 1
        while self.label() != '/expressionList':
            if self.label() == 'expression':
                self.parse_expression()
            self.pointer += 1

    def parse_expression(self):
        pointer += 1
        while self.label(pointer) != '/expression':
            if self.label(pointer) == 'term':
                pointer = self.parse_term(pointer)
            elif (self.label(pointer) == 'symbol') & (self.value(pointer) in self.commands):
                self.vm.append(self.commands[self.value(pointer)])
                pointer += 1
            pointer += 1
        return pointer

    def parse_term(self, pointer):
        pointer += 1
        if self.label(pointer) == 'expression':
            pointer = self.parse_expression(pointer)
        elif self.label(pointer) == 'integerConstant':
            self.vm.append('push' + self.value(pointer))
            pointer += 1
        elif self.label(pointer) == '/term':
            return pointer
        return pointer

    def parse_return(self, pointer):
        self.vm.append('return')
        return pointer

    def getVM(self):
        return self.vm
