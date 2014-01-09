from simplexn import *
from larcc import *

V = [[0.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, 0.0, 2.0], [0.0, 0.0, 3.0], [0.0, 0.0, 4.0], [0.0, 1.0, 0.0], [0.0, 1.0, 1.0], [0.0, 1.0, 2.0], [0.0, 1.0, 3.0], [0.0, 1.0, 4.0], [0.0, 2.0, 0.0], [0.0, 2.0, 1.0], [0.0, 2.0, 2.0], [0.0, 2.0, 3.0], [0.0, 2.0, 4.0], [1.0, 0.0, 0.0], [1.0, 0.0, 1.0], [1.0, 0.0, 2.0], [1.0, 0.0, 3.0], [1.0, 0.0, 4.0], [1.0, 1.0, 0.0], [1.0, 1.0, 1.0], [1.0, 1.0, 2.0], [1.0, 1.0, 3.0], [1.0, 1.0, 4.0], [1.0, 2.0, 0.0], [1.0, 2.0, 1.0], [1.0, 2.0, 2.0], [1.0, 2.0, 3.0], [1.0, 2.0, 4.0], [2.0, 0.0, 0.0], [2.0, 0.0, 1.0], [2.0, 0.0, 2.0], [2.0, 0.0, 3.0], [2.0, 0.0, 4.0], [2.0, 1.0, 0.0], [2.0, 1.0, 1.0], [2.0, 1.0, 2.0], [2.0, 1.0, 3.0], [2.0, 1.0, 4.0], [2.0, 2.0, 0.0], [2.0, 2.0, 1.0], [2.0, 2.0, 2.0], [2.0, 2.0, 3.0], [2.0, 2.0, 4.0], [3.0, 0.0, 0.0], [3.0, 0.0, 1.0], [3.0, 0.0, 2.0], [3.0, 0.0, 3.0], [3.0, 0.0, 4.0], [3.0, 1.0, 0.0], [3.0, 1.0, 1.0], [3.0, 1.0, 2.0], [3.0, 1.0, 3.0], [3.0, 1.0, 4.0], [3.0, 2.0, 0.0], [3.0, 2.0, 1.0], [3.0, 2.0, 2.0], [3.0, 2.0, 3.0], [3.0, 2.0, 4.0], [4.0, 0.0, 0.0], [4.0, 0.0, 1.0], [4.0, 0.0, 2.0], [4.0, 0.0, 3.0], [4.0, 0.0, 4.0], [4.0, 1.0, 0.0], [4.0, 1.0, 1.0], [4.0, 1.0, 2.0], [4.0, 1.0, 3.0], [4.0, 1.0, 4.0], [4.0, 2.0, 0.0], [4.0, 2.0, 1.0], [4.0, 2.0, 2.0], [4.0, 2.0, 3.0], [4.0, 2.0, 4.0]]
CV = [[0, 1, 5, 6, 15, 16, 20, 21], [1, 2, 6, 7, 16, 17, 21, 22], [3, 4, 8, 9, 18, 19, 23, 24], [5, 6, 10, 11, 20, 21, 25, 26], [6, 7, 11, 12, 21, 22, 26, 27], [8, 9, 13, 14, 23, 24, 28, 29], [15, 16, 20, 21, 30, 31, 35, 36], [16, 17, 21, 22, 31, 32, 36, 37], [18, 19, 23, 24, 33, 34, 38, 39], [20, 21, 25, 26, 35, 36, 40, 41], [21, 22, 26, 27, 36, 37, 41, 42], [23, 24, 28, 29, 38, 39, 43, 44], [45, 46, 50, 51, 60, 61, 65, 66], [46, 47, 51, 52, 61, 62, 66, 67], [48, 49, 53, 54, 63, 64, 68, 69], [50, 51, 55, 56, 65, 66, 70, 71], [51, 52, 56, 57, 66, 67, 71, 72], [53, 54, 58, 59, 68, 69, 73, 74]]

simplices = pivotSimplices(V,CV)

VIEW(STRUCT([
			 MKPOL([V,AA(AA(lambda k:k+1))(simplices),[]]),
			 SKEL_1(STRUCT(MKPOLS((V,CV))))
			 ]))



