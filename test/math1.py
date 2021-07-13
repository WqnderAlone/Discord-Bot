from sympy.solvers import solve
from sympy.abc import x, y, z, a, b
from sympy import solve, Poly, Eq, Function, exp
import sympy
import math

def solve(equationType, equation):
	if ("alg" in equationType):
		solution = sympy.solvers.solvers.solve(equation, x, set = True)
		return (f"`{solution}`")
	elif ("calc" in equationType):
		return(eval(equation))
