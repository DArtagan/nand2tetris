// PROGRAMMER: William H. Weiskopf
// USERID: WWEISKOP
// COURSE: CSCI-410
// TERM: FALL 2013
// This file is based on a file from www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[3], respectively.)

	@count  // number of summations to date
	M=1 	// set count to 0
	@R2  	// sum of R0 repeated R1 times
	M=0 	// set R2 to 0
	@R0		// load R0 into A
	D=M 	// set D = R0
	@END 	// load END into jump instruction
	D;JEQ 	// if R0 = 0, jump to END
	@R1 	// load R1 into A
	D=M 	// set D = R1
	@END 	// load END int jump instruction
	D;JEQ 	// if R1 = 0, jump to END
(LOOP)
	@count 	// load the current count into M
	D=M 	// set D = count
	@R1		// load R1 (repetition max) into A
	D=D-M	// D = count - R1
	@END	// load END into jump instruction
	D;JGT	// jump if (count - R1) > 0
	@R0  	// load R0 into M
	D=M 	// set D = R0
	@R2 	// load sum into M
	M=D+M 	// sum = R0 + sum
	@count	// load count into M
	M=M+1	// increment count
	@LOOP 	// load LOOP into jump instruction
	0;JMP 	// jump to LOOP
(END)
	@END
	0;JMP 	// infinite loop, standard Hack ending