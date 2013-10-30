// PROGRAMMER: William H. Weiskopf
// USERID: WWEISKOP
// COURSE: CSCI-410
// TERM: FALL 2013

	@0
	D = M
	@NEGATIVE
	D;JLT
	@POSITIVE
	D;JGE
(NEGATIVE)
	@0
	D = M
	M = D + M
	M = M + 1
	@END
	0;JMP
(POSITIVE)
	@0
	D = M
	M = D + M
(END)
	@END
	0;JMP 	// infinite loop, standard Hack ending