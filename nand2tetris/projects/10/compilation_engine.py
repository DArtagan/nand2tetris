#============================================================
# PROGRAMMER:........ William H. Weiskopf
# USERID:............ WWEISKOP
# COURSE:............ CSCI-410
# TERM............... FALL 2013
# ASIGNMENT:......... ECS 10
# FILENAME:.......... compilation_engine.py
# PYTHON VERSION:.... 3.3.0
#============================================================
class Grammarizer:
    token_pointer = 0
    xml = [ ]

    def __init__(self, jack_tokens):
        self.jack_tokens = jack_tokens
        for jack_token in self.jack_tokens:
            jack_token.getValue()
        self.parser(self.jack_tokens)

    def write(self, out_file):
        out = open(out_file, 'w')
        for jack_token in self.xml:
            out.write(str(jack_token) + '\n')


    def parser(self, jack_tokens):
        while self.token_pointer < len(self.jack_tokens):
            if (jack_token.getFlavour() == 'keyword') & (jack_token.getValue() == 'class'):
                parse_class()
            elif jack_token.get_flavour() == 'identifier':
                parse_identifier(jack_token.get_value())

    def parse_class(self):
        xml += '<class>'
        self.parser(self.jack_tokens[self.token_pointer:])
        xml += '</class>'

    def parse_identifier(self, value):
        xml += '<identifier> {0} </identifier>'.format(value) 
