// PROGRAMMER: William H. Weiskopf
// USERID: WWEISKOP
// COURSE: CSCI-410
// TERM: FALL 2013
	
	@1
	D = M
	@END
	D;JLE		// Check if n is negative or zero
	@11
	M = -1
	D = M
	M = D + M	// R12 = -2
	@12
	M = 1
	D = M
	M = M + D
	D = M + D
	M = M + D
	D = M + D
	M = M + D
	M = M + 1
	M = M + 1
	M = M + 1 	// R12 = 16
	D = M
	@1
	D = M
	@13
	M = D		// R13 = R1
	@1
	D = M + 1
	@12
	D = M
	@13
	D = D - M
	@14
	M = D		// R14 = 16 - R1
	@1
	D = M
	@12
	M = M - D 	// R12 = 15
(ONELOOP)
	@0
	D = M
	@ONEPOSITIVE
	D;JGE
(ONENEGATIVE)
	@0
	D = M
	M = D + M
	M = M + 1
	@ONELOOPEND
	0;JMP
(ONEPOSITIVE)
	@0
	D = M
	M = D + M
(ONELOOPEND)
	@12
	M = M - 1
	D = M
	@ONELOOP
	D;JGT
(TWOLOOP)
	@0
	D = M
	@TWOPOSITIVE
	D;JGE
(TWONEGATIVE)
	@0
	D = M
	M = D + M
	M = M + 1
	@TWOLOOPEND
	0;JMP
(TWOPOSITIVE)
	@0
	D = M
	M = D + M
(TWOLOOPEND)
	@11
	D = M
	@0
	M = D & M
	@13
	M = M - 1
	D = M
	@TWOLOOP
	D;JGT
(THREELOOP)
	@0
	D = M
	@THREEPOSITIVE
	D;JGE
(THREENEGATIVE)
	@0
	D = M
	M = D + M
	M = M + 1
	@THREELOOPEND
	0;JMP
(THREEPOSITIVE)
	@0
	D = M
	M = D + M
(THREELOOPEND)
	@14
	M = M - 1
	D = M
	@THREELOOP
	D;JGT
(END)
	@END
	0;JMP 		// infinite loop, standard Hack ending