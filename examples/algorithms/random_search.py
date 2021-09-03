from pymoo.algorithms.soo.nonconvex.random_search import RandomSearch
from pymoo.factory import get_problem
from pymoo.operators.sampling.lhs import LHS

from pymoo.optimize import minimize


problem = get_problem("ackley")

algorithm = RandomSearch(
    n_points_per_iteration=100,
    sampling=LHS()
)

res = minimize(problem,
               algorithm,
               ("n_gen", 5),
               seed=1,
               verbose=False)

print("Best solution found: \nX = %s\nF = %s" % (res.X, res.F))