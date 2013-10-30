#============================================================
# PROGRAMMER:........ William H. Weiskopf
# USERID:............ WWEISKOP
# COURSE:............ CSCI-410
# TERM............... FALL 2013
# ASIGNMENT:......... ECS 07
# FILENAME:.......... boolean.py
# PYTHON VERSION:.... 3.3.0
#============================================================

class boolean:
    binary_boolean = ("@SP\n"
                      "M=M-1\n"
                      "A=M\n"
                      "D=M\n"
                      "@SP\n"
                      "M=M-1\n"
                      "A=M\n"
                      "D=M-D\n"
                      "@{0}\n"   # true_label
                      "D;{1}\n"  # jmp
                      "@0\n"
                      "D=A\n"
                      "@{2}\n"   # end_label
                      "0;JMP\n"
                      "({0})\n"  # true_label
                      "@0\n"
                      "D=!A\n"
                      "({2})\n"  # end_label
                      "@SP\n"
                      "A=M\n"
                      "M=D\n"
                      "@SP\n"
                      "M=M+1\n")

    def equality(count):
        return boolean.boolean("JEQ", count) 

    def greater_than(count):
        return boolean.boolean("JGT", count)

    def less_than(count):
        return boolean.boolean("JLT", count)

    def boolean(jmp, count):
        return boolean.binary_boolean.format( "boolean_" + str(count) + "_true", jmp, "boolean_" + str(count) + "_end" )
