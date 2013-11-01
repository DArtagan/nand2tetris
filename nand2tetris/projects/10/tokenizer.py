from lexer import *

class Tokenizer:

    def __init__(self, in_file):
        self.lexer = Lexer(in_file, out_file)

    def __str__(self):
        return self.lexer
