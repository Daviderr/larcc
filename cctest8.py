from smplxn import *

geom_0,topol_0 = [[0.],[1.],[2.],[3.],[4.]],[[0,1],[1,2],[3,4]]
geom_1,topol_1 = [[0.],[1.],[2.]], [[0,1],[1,2]]
mod_0 = (geom_0,topol_0)
mod_1 = (geom_1,topol_1)
#--------------------------------------------------------------
squares = larProduct([mod_0,mod_1])
V,FV = squares
simplices = pivotSimplices(V,FV,d=2)

VIEW(STRUCT([
	 MKPOL([V,AA(AA(C(SUM)(1)))(simplices),[]]),
	 SKEL_1(STRUCT(MKPOLS((V,FV))))
			 ]))
#--------------------------------------------------------------
# cubes = INSL(larProduct)([mod_0,mod_1,mod_0]) # ==
cubes = larProduct([squares,mod_0])
V,CV = cubes
simplices = pivotSimplices(V,CV,d=3)

VIEW(STRUCT([
			 MKPOL([V,AA(AA(C(SUM)(1)))(simplices),[]]),
			 SKEL_1(STRUCT(MKPOLS((V,CV))))
			 ]))
#--------------------------------------------------------------
