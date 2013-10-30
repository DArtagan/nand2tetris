// PROGRAMMER: William H. Weiskopf
// USERID: WWEISKOP
// COURSE: CSCI-410
// TERM: FALL 2013

	@1
	D = M
	@11
	M = D
	@END
	D;JLE	// Check if n is negative or zero
(LOOP)
	@0
	D = M
	M = D + M
	@11
	M = M - 1
	D = M
	@LOOP
	D;JGT
(END)
	@END
	0;JMP 	// infinite loop, standard Hack ending