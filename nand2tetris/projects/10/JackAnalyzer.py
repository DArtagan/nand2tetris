#============================================================
# PROGRAMMER:........ William H. Weiskopf
# USERID:............ WWEISKOP
# COURSE:............ CSCI-410
# TERM............... FALL 2013
# ASIGNMENT:......... ECS 10
# FILENAME:.......... JackAnalyzer.py
# PYTHON VERSION:.... 3.3.0
#============================================================
import sys
import os
from tokenizer import JackTokenizer
from compilation_engine import Grammarizer

class SyntaxAnalyzer:
    def __init__(self, in_file):
        self.jack_tokens = JackTokenizer(in_file).getJackTokens()
        self.xml = Grammarizer(self.jack_tokens).getXML()

    def __str__(self):
        return str(self.jack_tokens)

    def write(self, out_file):
        out = open(out_file, 'w')
        # for jack_token in self.jack_tokens:
        #     out.write(str(jack_token) + '\n')
        for line in self.xml:
            out.write(str(line) + '\n')

class fileSet:
    files = []
    dir_name = ""
    dir_check = False
    
    def __init__(self):
        argument = sys.argv
        if((len(argument) < 2) | (len(argument) > 2)):
            print('Please use one properly formatted directory.')
        else:
            argument = argument[1]
            if(os.path.isdir(argument)):
                os.chdir(argument)
                self.dir_name = argument
                for name in os.listdir('.'):
                    if os.path.isfile(name) & (".jack" in name):
                        self.files.append(name)
                self.dir_check = True
            elif(os.path.isfile(argument)):
                self.files.append(argument)
            else:
                print("Error parsing given folder.")

    def get_files(self):
        return self.files

    def get_dirname(self):
        return self.dir_name

    def is_dir(self):
        return self.dir_check


##########
# MAIN PROGRAM
##########

in_files = fileSet().get_files()
for da_file in in_files:
    SyntaxAnalyzer(da_file).write(da_file[:-5] + "-tokens.xml")
