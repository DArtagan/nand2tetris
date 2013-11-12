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
    def __init__(self, jack_tokens):
        self.xml = []
        self.pointer = 0
        self.jack_tokens = jack_tokens
        self.parser()

    def write(self, out_file):
        out = open(out_file, 'w')
        for jack_token in self.xml:
            out.write(str(jack_token) + '\n')

    def parser(self):
        if self.jack_tokens[self.pointer] == JackToken('keyword', 'class'):
            self.class_parser()
        
    def check_token(self, flavour, value):
        pass 

    def class_parser(self):
        self.xml.append('<class>')
        self.xml.append(self.jack_tokens[pointer])
        self.pointer += 1
        self.xml.append(self.jack_tokens[pointer])
        self.pointer += 1
        self.xml.append(self.jack_tokens[pointer])
        self.pointer += 1
        while (self.jack_tokens[self.pointer] == JackToken('keyword', 'static')) | (self.jack_tokens[self.pointer] == JackToken('keyword', 'field')):
            parse_classVarDec()
        self.parser(jack_tokens[1:])
        self.xml.append('</class>')
