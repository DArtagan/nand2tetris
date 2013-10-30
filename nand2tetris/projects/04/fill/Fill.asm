// PROGRAMMER: William H. Weiskopf
// USERID: WWEISKOP
// COURSE: CSCI-410
// TERM: FALL 2013
// This file is based on a file from www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, the
// program clears the screen, i.e. writes "white" in every pixel.

@R0			// initialization check bit
M=0
@R1			// screen word counter
M=0
(INPUT)
	@KBD
	D=M
	@WHITEPICK
	D;JLE
	@BLACKPICK
	D;JGT
(WHITEPICK)
	@R0
	D=M
	@WHITEINIT
	D;JLE
	@WHITEN
	D;JGT
(BLACKPICK)
	@R0
	D=M
	@BLACKINIT
	D;JGE
	@BLACKEN
	D;JLT
(WHITEINIT)
	@R0
	M=1
	@SCREEN
	M=0
	D=A 	// D will be the address counter
	@R1
	M=D
	@INPUT
	0;JMP
(BLACKINIT)
	@R0
	M=-1
	@SCREEN
	M=-1
	D=A 	// D will be the address counter
	@R1
	M=D
	@INPUT
	0;JMP
(WHITEN)	// white loop
	@R1
	M=M+1
	D=M
	A=D
	M=0
	@24575
	D=D-A
	@WHITEINIT
	D;JGE
	@INPUT
	0;JMP
(BLACKEN)	// black Loop
	@R1
	M=M+1
	D=M
	A=D
	M=-1
	@24575
	D=D-A
	@BLACKINIT
	D;JGE
	@INPUT
	0;JMP