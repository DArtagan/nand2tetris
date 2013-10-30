// PROGRAMMER: William H. Weiskopf
// USERID: WWEISKOP
// COURSE: CSCI-410
// TERM: FALL 2013

	@11
	M = -1
	D = M
	M = D + M	// R11 = -2
	@12
	M = 0		// R12 = quotient
(LOOP)
	@12
	M = M + 1
	@11
	D = M
	@0
	M = D + M
	D = M
	@11
	D = M + D
	@OUTSIDELOOP 
	D;JLT 		// if D < 0, jump to OUTERLOOP
	@LOOP
	D;JGE		// if D >= 0, repeat INNERLOOP
(OUTSIDELOOP)
	@12
	D = M
	@0
	M = D
(END)
	@END
	0;JMP 	// infinite loop, standard Hack ending