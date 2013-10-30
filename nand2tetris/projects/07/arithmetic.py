#============================================================
# PROGRAMMER:........ William H. Weiskopf
# USERID:............ WWEISKOP
# COURSE:............ CSCI-410
# TERM............... FALL 2013
# ASIGNMENT:......... ECS 07
# FILENAME:.......... arithmetic.py
# PYTHON VERSION:.... 3.3.0
#============================================================

class arithmetic:
    binary = ("@SP\n"
              "M=M-1\n"
              "A=M\n"
              "D=M\n"
              "@SP\n"
              "M=M-1\n"
              "A=M\n"
              "D=M{0}D\n"
              "@SP\n"
              "A=M\n"
              "M=D\n"
              "@SP\n"
              "M=M+1\n")

    unary = ("@SP\n"
             "M=M-1\n"
             "A=M\n"
             "D={0}M\n"
             "@SP\n"
             "A=M\n"
             "M=D\n"
             "@SP\n"
             "M=M+1\n"
            )

    def addition():
        return arithmetic.binary.format("+")

    def subtraction():
        return arithmetic.binary.format("-")

    def and_arith():
        return arithmetic.binary.format("&")

    def or_arith():
        return arithmetic.binary.format("|")

    def negative():
        return arithmetic.unary.format("-")

    def not_arith(): 
        return arithmetic.unary.format("!")
