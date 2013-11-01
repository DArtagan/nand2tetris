import sys
import os
from tokenizer import *

class SyntaxAnalyzer:
    def __init__(self, in_file):
        self.tokens = Tokenizer(in_file)

    def __str__(self):
        return self.tokens

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
                    if os.path.isfile(name) & (".vm" in name):
                        self.files.append(name)
                self.dir_check = True
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

in_files = fileSet()
for da_file in in_files.get_files():
    print(SyntaxAnalyzer(da_file))
