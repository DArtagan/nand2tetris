@0
@1639
@3278
@4917
@6556
@8195
@9834
@11473
@13112
@14751
@16390
@18029
@19668
@21307
@22946
@24585
@26224
@27863
@29502
@31141
D&A
A=X01;JNE
M=D+A;JEQ
AM=X03;JMP
D=X04;JLT
AMD=X05;JGT
MD=X06;JLE
A-D;JGE
AM=X08
M=X09;JNE
AD=X0A;JEQ
D=X0B;JMP
AMD=D;JLT
A=!D;JGT
D-1;JLE
AM=-D;JGE
D=X10
AD=X11;JNE
MD=X12;JEQ
AMD=D-A;JMP
A=X14;JLT
M=D|A;JGT
AM=X16;JLE
D=X17;JGE
AMD=X18
MD=X19;JNE
X1A;JEQ
A=X1B;JMP
M=X1C;JLT
AD=X1D;JGT
D=X1E;JLE
AMD=D+1;JGE
A=X20
X21;JNE
AM=X22;JEQ
M=X23;JMP
AD=X24;JLT
MD=X25;JGT
AMD=X26;JLE
A=X27;JGE
M=X28
AM=X29;JNE
D=0;JEQ
AD=X2B;JMP
MD=X2C;JLT
X2D;JGT
A=X2E;JLE
M=X2F;JGE
AD=A
D=X31;JNE
AMD=A-1;JEQ
MD=-A;JMP
X34;JLT
AM=X35;JGT
M=X36;JLE
AD=A+1;JGE
MD=X38
AMD=X39;JNE
A=-1;JEQ
X3B;JMP
AM=X3C;JLT
D=X3D;JGT
AD=X3E;JLE
MD=1;JGE
D&M
A=X41;JNE
M=D+M;JEQ
AM=X43;JMP
D=X44;JLT
AMD=X45;JGT
MD=X46;JLE
M-D;JGE
AM=X48
M=X49;JNE
AD=X4A;JEQ
D=X4B;JMP
AMD=X4C;JLT
A=X4D;JGT
X4E;JLE
AM=X4F;JGE
D=X50
AD=X51;JNE
MD=X52;JEQ
AMD=D-M;JMP
A=X54;JLT
M=D|M;JGT
AM=X56;JLE
D=X57;JGE
AMD=X58
MD=X59;JNE
X5A;JEQ
A=X5B;JMP
M=X5C;JLT
AD=X5D;JGT
D=X5E;JLE
AMD=X5F;JGE
A=X60
X61;JNE
AM=X62;JEQ
M=X63;JMP
AD=X64;JLT
MD=X65;JGT
AMD=X66;JLE
A=X67;JGE
M=X68
AM=X69;JNE
D=X6A;JEQ
AD=X6B;JMP
MD=X6C;JLT
X6D;JGT
A=X6E;JLE
M=X6F;JGE
AD=M
D=!M;JNE
AMD=M-1;JEQ
MD=-M;JMP
X74;JLT
AM=X75;JGT
M=X76;JLE
AD=M+1;JGE
MD=X78
AMD=X79;JNE
A=X7A;JEQ
X7B;JMP
AM=X7C;JLT
D=X7D;JGT
AD=X7E;JLE
MD=X7F;JGE