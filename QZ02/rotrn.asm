// PROGRAMMER: William H. Weiskopf
// USERID: WWEISKOP
// COURSE: CSCI-410
// TERM: FALL 2013
	
	@1
	D = M
	@12
	M = D
	@END
	D;JLE	// Check if n is negative or zero
	@11
	M = 1
	D = M
	M = M + D
	D = M + D
	M = M + D
	D = M + D
	M = M + D
	M = M + 1
	M = M + 1
	D = M + 1
	@12
	M = D - M
(LOOP)
	@0
	D = M
	@POSITIVE
	D;JGE
(NEGATIVE)
	@0
	D = M
	M = D + M
	M = M + 1
	@LOOPEND
	0;JMP
(POSITIVE)
	@0
	D = M
	M = D + M
(LOOPEND)
	@12
	M = M - 1
	D = M
	@LOOP
	D;JGT
(END)
	@END
	0;JMP 	// infinite loop, standard Hack ending