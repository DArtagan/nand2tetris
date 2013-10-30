#============================================================
# PROGRAMMER:........ William H. Weiskopf
# USERID:............ WWEISKOP
# COURSE:............ CSCI-410
# TERM............... FALL 2013
# ASIGNMENT:......... ECS 07
# FILENAME:.......... memory.py
# PYTHON VERSION:.... 3.3.0
#============================================================

class memory:
    push = ("@{0}\n"
            "D={1}\n"
            "@SP\n"
            "A=M\n"
            "M=D\n"
            "@SP\n"
            "M=M+1\n"
           )

    pop1 = ("@SP\n"
           "M=M-1\n"
           "A=M\n"
           "D=M\n"
           "@{0}\n"
           "M=D\n"
          )

    temps = {"0": "R5",
             "1": "R6",
             "2": "R7",
             "3": "R8",
             "4": "R9",
             "5": "R10",
             "6": "R11",
             "7": "R12",
            }

    pointers = {"0": "R3",
                "1": "R4",
               }

    push_special = ("M\n"
                    "@{0}\n"
                    "A=A+D\n"
                    "D=M"
                   )

    pop2 = ("@{0}\n"
            "D=M\n"
            "@{1}\n"
            "D=A+D\n"
            "@SP\n"
            "A=M\n"
            "M=D\n"
            "@SP\n"
            "A=M-1\n"
            "D=M\n"
            "@SP\n"
            "A=M\n"
            "M=D\n"
            "@SP\n"
            "M=M-1\n"
           )

    # segments = {"constant", self.segment_constant,
    #             "static", self.segment_static,
    #             "temp", self.segment_temp,
    #             "pointer", self.segment_pointer,
    #             "argument", self.segment_argument,
    #             "local", self.segment_local,
    #             "this", self.segment_this,
    #             "that", self.segment_that, }

    def push_constant(index):
        return memory.push.format(index, "A")

    def push_static(index):
        return memory.push.format("TRANSLATOR_LABEL_" + index, "M")

    def push_temp(index):
        return memory.push.format(memory.temps[index], "M")

    def push_pointer(index):
        return memory.push.format(memory.pointers[index], "M")

    def push_argument(index):
        return memory.push.format("ARG", memory.push_special.format(index))
    
    def push_local(index):
        return memory.push.format("LCL", memory.push_special.format(index))
    
    def push_this(index):
        return memory.push.format("THIS", memory.push_special.format(index))
    
    def push_that(index):
        return memory.push.format("THAT", memory.push_special.format(index))
                
    def pop_constant(index):
        return memory.pop1.format(index)

    def pop_static(index):
        return memory.pop1.format("TRANSLATOR_LABEL_" + index)

    def pop_temp(index):
        return memory.pop1.format(memory.temps[index])

    def pop_pointer(index):
        return memory.pop1.format(memory.pointers[index])

    def pop_argument(index):
        return memory.pop2.format("ARG", index)
    
    def pop_local(index):
        return memory.pop2.format("LCL", index)
    
    def pop_this(index):
        return memory.pop2.format("THIS", index)
    
    def pop_that(index):
        return memory.pop2.format("THAT", index)
