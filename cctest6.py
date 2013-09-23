from smplxn import *

V = [[4, 10, 0.0*2],
 [4, 10, 1.0*2],
 [4, 10, 2.0*2],
 [8, 10, 0.0*2],
 [8, 10, 1.0*2],
 [8, 10, 2.0*2],
 [14, 10, 0.0*2],
 [14, 10, 1.0*2],
 [14, 10, 2.0*2],
 [8, 7, 0.0*2],
 [8, 7, 1.0*2],
 [8, 7, 2.0*2],
 [14, 7, 0.0*2],
 [14, 7, 1.0*2],
 [14, 7, 2.0*2],
 [4, 4, 0.0*2],
 [4, 4, 1.0*2],
 [4, 4, 2.0*2],
 [8, 4, 0.0*2],
 [8, 4, 1.0*2],
 [8, 4, 2.0*2],
 [14, 4, 0.0*2],
 [14, 4, 1.0*2],
 [14, 4, 2.0*2]]

CV = [[0, 1, 3, 4, 9, 10, 15, 16, 18, 19], [1, 2, 4, 5, 10, 11, 16, 17, 19, 20], [3, 4, 6, 7, 9, 10, 12, 13], [4, 5, 7, 8, 10, 11, 13, 14], [9, 10, 12, 13, 18, 19, 21, 22], [10, 11, 13, 14, 19, 20, 22, 23]]


FV = [[0, 3, 9, 15, 18], [1, 4, 10, 16, 19], [2, 5, 11, 17, 20], [3, 6, 9, 12], [4, 7, 10, 13], [5, 8, 11, 14], [9, 12, 18, 21], [10, 13, 19, 22], [11, 14, 20, 23], [0, 1, 3, 4], [0, 1, 15, 16], [1, 2, 4, 5], [1, 2, 16, 17], [3, 4, 6, 7], [3, 4, 9, 10], [4, 5, 7, 8], [4, 5, 10, 11], [6, 7, 12, 13], [7, 8, 13, 14], [9, 10, 12, 13], [9, 10, 18, 19], [10, 11, 13, 14], [10, 11, 19, 20], [12, 13, 21, 22], [13, 14, 22, 23], [15, 16, 18, 19], [16, 17, 19, 20], [18, 19, 21, 22], [19, 20, 22, 23]]

EV = [[0, 3], [0, 15], [1, 4], [1, 16], [2, 5], [2, 17], [3, 6], [3, 9], [4, 7], [4, 10], [5, 8], [5, 11], [6, 12], [7, 13], [8, 14], [9, 12], [9, 18], [10, 13], [10, 19], [11, 14], [11, 20], [12, 21], [13, 22], [14, 23], [15, 18], [16, 19], [17, 20], [18, 21], [19, 22], [20, 23], [0, 1], [1, 2], [3, 4], [4, 5], [6, 7], [7, 8], [9, 10], [10, 11], [12, 13], [13, 14], [15, 16], [16, 17], [18, 19], [19, 20], [21, 22], [22, 23]]


simplices = pivotSimplices(V,CV,d=3)

VIEW(STRUCT([
			 MKPOL([V,AA(AA(lambda k:k+1))(simplices),[]]),
			 STRUCT(MKPOLS((V,EV)))
			 ]))

print "\nsimplexOrientations(simplices) =",simplexOrientations(V,simplices),"\n"


