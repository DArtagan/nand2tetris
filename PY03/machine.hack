0000000000000000 @0
0000011001100111 @1639
0000110011001110 @3278
0001001100110101 @4917
0001100110011100 @6556
0010000000000011 @8195
0010011001101010 @9834
0010110011010001 @11473
0011001100111000 @13112
0011100110011111 @14751
0100000000000110 @16390
0100011001101101 @18029
0100110011010100 @19668
0101001100111011 @21307
0101100110100010 @22946
0110000000001001 @24585
0110011001110000 @26224
0110110011010111 @27863
0111001100111110 @29502
0111100110100101 @31141
1110000000000000 D&A
1110000001100101 A=X01;JNE
1110000010001010 M=D+A;JEQ
1110000011101111 AM=X03;JMP
1110000100010100 D=X04;JLT
1110000101111001 AMD=X05;JGT
1110000110011110 MD=X06;JLE
1110000111000011 A-D;JGE
1110001000101000 AM=X08
1110001001001101 M=X09;JNE
1110001010110010 AD=X0A;JEQ
1110001011010111 D=X0B;JMP
1110001100111100 AMD=D;JLT
1110001101100001 A=!D;JGT
1110001110000110 D-1;JLE
1110001111101011 AM=-D;JGE
1110010000010000 D=X10
1110010001110101 AD=X11;JNE
1110010010011010 MD=X12;JEQ
1110010011111111 AMD=D-A;JMP
1110010100100100 A=X14;JLT
1110010101001001 M=D|A;JGT
1110010110101110 AM=X16;JLE
1110010111010011 D=X17;JGE
1110011000111000 AMD=X18
1110011001011101 MD=X19;JNE
1110011010000010 X1A;JEQ
1110011011100111 A=X1B;JMP
1110011100001100 M=X1C;JLT
1110011101110001 AD=X1D;JGT
1110011110010110 D=X1E;JLE
1110011111111011 AMD=D+1;JGE
1110100000100000 A=X20
1110100001000101 X21;JNE
1110100010101010 AM=X22;JEQ
1110100011001111 M=X23;JMP
1110100100110100 AD=X24;JLT
1110100101011001 MD=X25;JGT
1110100110111110 AMD=X26;JLE
1110100111100011 A=X27;JGE
1110101000001000 M=X28
1110101001101101 AM=X29;JNE
1110101010010010 D=0;JEQ
1110101011110111 AD=X2B;JMP
1110101100011100 MD=X2C;JLT
1110101101000001 X2D;JGT
1110101110100110 A=X2E;JLE
1110101111001011 M=X2F;JGE
1110110000110000 AD=A
1110110001010101 D=!A;JNE
1110110010111010 AMD=A-1;JEQ
1110110011011111 MD=-A;JMP
1110110100000100 X34;JLT
1110110101101001 AM=X35;JGT
1110110110001110 M=X36;JLE
1110110111110011 AD=A+1;JGE
1110111000011000 MD=X38
1110111001111101 AMD=X39;JNE
1110111010100010 A=-1;JEQ
1110111011000111 X3B;JMP
1110111100101100 AM=X3C;JLT
1110111101010001 D=X3D;JGT
1110111110110110 AD=X3E;JLE
1110111111011011 MD=1;JGE
1111000000000000 D&M
1111000001100101 A=X41;JNE
1111000010001010 M=D+M;JEQ
1111000011101111 AM=X43;JMP
1111000100010100 D=X44;JLT
1111000101111001 AMD=X45;JGT
1111000110011110 MD=X46;JLE
1111000111000011 M-D;JGE
1111001000101000 AM=X48
1111001001001101 M=X49;JNE
1111001010110010 AD=X4A;JEQ
1111001011010111 D=X4B;JMP
1111001100111100 AMD=X4C;JLT
1111001101100001 A=X4D;JGT
1111001110000110 X4E;JLE
1111001111101011 AM=X4F;JGE
1111010000010000 D=X50
1111010001110101 AD=X51;JNE
1111010010011010 MD=X52;JEQ
1111010011111111 AMD=D-M;JMP
1111010100100100 A=X54;JLT
1111010101001001 M=D|M;JGT
1111010110101110 AM=X56;JLE
1111010111010011 D=X57;JGE
1111011000111000 AMD=X58
1111011001011101 MD=X59;JNE
1111011010000010 X5A;JEQ
1111011011100111 A=X5B;JMP
1111011100001100 M=X5C;JLT
1111011101110001 AD=X5D;JGT
1111011110010110 D=X5E;JLE
1111011111111011 AMD=X5F;JGE
1111100000100000 A=X60
1111100001000101 X61;JNE
1111100010101010 AM=X62;JEQ
1111100011001111 M=X63;JMP
1111100100110100 AD=X64;JLT
1111100101011001 MD=X65;JGT
1111100110111110 AMD=X66;JLE
1111100111100011 A=X67;JGE
1111101000001000 M=X68
1111101001101101 AM=X69;JNE
1111101010010010 D=X6A;JEQ
1111101011110111 AD=X6B;JMP
1111101100011100 MD=X6C;JLT
1111101101000001 X6D;JGT
1111101110100110 A=X6E;JLE
1111101111001011 M=X6F;JGE
1111110000110000 AD=M
1111110001010101 D=!M;JNE
1111110010111010 AMD=M-1;JEQ
1111110011011111 MD=-M;JMP
1111110100000100 X74;JLT
1111110101101001 AM=X75;JGT
1111110110001110 M=X76;JLE
1111110111110011 AD=M+1;JGE
1111111000011000 MD=X78
1111111001111101 AMD=X79;JNE
1111111010100010 A=X7A;JEQ
1111111011000111 X7B;JMP
1111111100101100 AM=X7C;JLT
1111111101010001 D=X7D;JGT
1111111110110110 AD=X7E;JLE
1111111111011011 MD=X7F;JGE
