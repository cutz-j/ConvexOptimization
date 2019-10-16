import cvxpy as cp
import numpy as np

x1 = cp.Variable()
x2 = cp.Variable()
constraints = [2*x1 + x2 >= 1, x1 + 3*x2 >= 1, x1 >= 0, x2 >= 0]

## a ##
objective = cp.Minimize(x1+x2)
p = cp.Problem(objective, constraints)
res = p.solve()
print(res)
