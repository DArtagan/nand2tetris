@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@7777
@0
D=A
@LCL
A=M
D=D+A
@SP
A=M
M=D
@SP
M=M-1
A=M
D=M
@SP
A=M+1
A=M
M=D
@7777
(LOOP_START)
@7777
@ARG
D=M
@0
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1
@7777
@LCL
D=M
@0
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1
@7777
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=M+D
@SP
A=M
M=D
@SP
M=M+1
@7777
@0	
D=A
@LCL
A=M
D=D+A
@SP
A=M
M=D
@SP
M=M-1
A=M
D=M
@SP
A=M+1
A=M
M=D
@7777
@ARG
D=M
@0
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1
@7777
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
@7777
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=M-D
@SP
A=M
M=D
@SP
M=M+1
@7777
@0
D=A
@ARG
A=M
D=D+A
@SP
A=M
M=D
@SP
M=M-1
A=M
D=M
@SP
A=M+1
A=M
M=D
@7777
@ARG
D=M
@0
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1
@7777
@SP
M=M-1
A=M
D=M
@LOOP_START
D;JNE
@7777
@LCL
D=M
@0
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1
@7777
(END_LOOP)
@END_LOOP
0;JMP