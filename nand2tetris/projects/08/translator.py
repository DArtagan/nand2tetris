#============================================================
# PROGRAMMER:........ William H. Weiskopf
# USERID:............ WWEISKOP
# COURSE:............ CSCI-410
# TERM............... FALL 2013
# ASIGNMENT:......... ECS 08
# FILENAME:.......... translator.py
# PYTHON VERSION:.... 3.3.0
#============================================================

import re
import sys
import os
from memory import *
from arithmetic import *
from boolean import *

class stack:

    dict_arithmetic = {"add": arithmetic.addition,
                       "sub": arithmetic.subtraction,
                       "neg": arithmetic.negative,
                       "and": arithmetic.and_arith,
                       "or":  arithmetic.or_arith,
                       "not": arithmetic.not_arith, 
                      }

    dict_boolean = {"eq":  boolean.equality,
                    "gt":  boolean.greater_than,
                    "lt":  boolean.less_than,
                   }

    dict_memory = {"push_constant": memory.push_constant,
                   "push_static":   memory.push_static,
                   "push_temp":     memory.push_temp,
                   "push_pointer":  memory.push_pointer,
                   "push_argument": memory.push_argument,
                   "push_local":    memory.push_local,
                   "push_this":     memory.push_this,
                   "push_that":     memory.push_that, 
                   "push_pointer":  memory.push_pointer,
                   "pop_constant":  memory.pop_constant,
                   "pop_static":    memory.pop_static,
                   "pop_temp":      memory.pop_temp,
                   "pop_pointer":   memory.pop_pointer,
                   "pop_argument":  memory.pop_argument,
                   "pop_local":     memory.pop_local,
                   "pop_this":      memory.pop_this,
                   "pop_that":      memory.pop_that, 
               }

    def __init__(self):
        self.stack = ""
        self.bool_count = 0
        
    def read(self, in_file):
        self.in_file = open(in_file, 'r')
        if self.stack is "":
            self.initialization()
        self.parse()

    def initialization(self):
        self.stack += ("@256\n"
                       "D=A\n"
                       "@SP\n"
                       "M=D\n"
                      )
        self.call("Sys.init", "0")

    def parse(self):
        for line in self.in_file:
            line = line.strip()
            if line.startswith("//") | (line == ""):
                continue
            line = line.split(' ')
            if line[0] in self.dict_arithmetic:
                self.arithmetic(line[0])
            elif line[0] in self.dict_boolean:
                self.boolean(line[0])
            elif (line[0] == "push") | (line[0] == "pop"):
                self.memory(line[0], line[1], line[2])
            elif line[0] == "label":
                self.label(line[1])
            elif "goto" in line[0]:
                self.goto(line[0], line[1])
            elif line[0] == "function":
                self.function(line[1], line[2])
            elif line[0] == "return":
                self.func_return()
            elif line[0] == "call":
                self.call(line[1], line[2])
            #self.stack += "@7777\n"

    def close(self):
        self.stack += "(END_LOOP)\n@END_LOOP\n0;JMP"

    def __str__(self):
        return self.stack

    def write(self, out_file):
        out_file = open(out_file, 'w')
        out_file.write(str(self))

    def arithmetic(self, operation):
        self.stack += self.dict_arithmetic[operation]()

    def boolean(self, operation):
        self.stack += self.dict_boolean[operation](self.bool_count)
        self.bool_count += 1

    def memory(self, pushpop, segment, index):
        self.stack += self.dict_memory[pushpop + "_" + segment](index)

    def label(self, label):
        self.stack += "({0})\n".format(label)

    def goto(self, gotoType, label):
        if gotoType == "if-goto":
            self.stack += ("@SP\n"
                           "M=M-1\n"
                           "A=M\n"
                           "D=M\n"
                           "@{0}\n"
                           "D;JNE\n"
                          ).format(label)
        elif gotoType == "goto":
            self.stack += ("@{0}\n"
                           "0;JMP\n"
                          ).format(label)

    def function(self, name, args):
        self.label(name)
        for i in range(0, int(args)):
            self.memory("push", "constant", "0")

    def func_return(self):
        self.stack += ("@LCL\n"
                       "D=M\n"
                       "@FRAME\n"
                       "M=D\n"
                       "@5\n"
                       "A=D-A\n"
                       "D=M\n"
                       "@RETURN_ADDR\n"
                       "M=D\n"
                       "@SP\n"
                       "M=M-1\n"
                       "A=M\n"
                       "D=M\n"
                       "@ARG\n"
                       "A=M\n"
                       "M=D\n"
                       "@ARG\n"
                       "D=M+1\n"
                       "@SP\n"
                       "M=D\n"
                      )
        n = 1
        for function_stack in ["THAT", "THIS", "ARG", "LCL"]:
            self.stack += ("@FRAME\n"
                           "D=M\n"
                           "@{0}\n"
                           "A=D-A\n"
                           "D=M\n"
                           "@{1}\n"
                           "M=D\n"
                          ).format(n, function_stack)
            n += 1
        self.stack += ("@RETURN_ADDR\n"
                       "A=M\n"
                       "0;JMP\n"
                      )

    def call(self, name, args):
        self.memory("push", "constant", "return_" + name)
        self.memory("push", "pointer", "LCL")
        self.memory("push", "pointer", "ARG")
        self.memory("push", "pointer", "THIS")
        self.memory("push", "pointer", "THAT")
        self.stack += ("@SP\n"
                       "D=M\n"
                       "@5\n"
                       "D=D-A\n"
                       "@{0}\n"
                       "D=D-M\n"
                       "@ARG\n"
                       "M=D\n"
                       "@SP\n"
                       "D=M\n"
                       "@LCL\n"
                       "M=D\n").format(args)
        self.goto("goto", name)
        self.label("return_{0}".format(name))


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
newStack = stack()
for da_file in in_files.get_files():
    newStack.read(da_file)
newStack.close()
print(newStack)
outputFile = os.path.basename(os.path.normpath(in_files.get_dirname())) + '.asm' 
newStack.write(outputFile)

