from pymoo.algorithms.soo.nonconvex.pso import PSO
from pymoo.factory import Rastrigin
from pymoo.optimize import minimize

problem = Rastrigin()

algorithm = PSO(pop_size=25)

res = minimize(problem,
               algorithm,
               seed=1,
               verbose=True)

print("Best solution found: \nX = %s\nF = %s" % (res.X, res.F))
