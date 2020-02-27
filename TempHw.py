"""
This module implements local search on a simple sine function variant.  It uses
simulated annealing and hill climbing to do this.  It also implements random restarts
to average out the solutions and find a max over a given number of runs.

@author: Quentin Barnes
(Based on code by kvlinden)
"""
import math
import time
from search import Problem, hill_climbing, simulated_annealing, \
    exp_schedule, genetic_search
from random import randrange


# class AbsVariant(Problem):
#     """
#     State: x value for the abs function variant f(x)
#     Move: a new x value delta steps from the current x (in both directions)
#     """

#     def __init__(self, initial, maximum=30.0, delta=0.001):
#         self.initial = initial
#         self.maximum = maximum
#         self.delta = delta

#     def actions(self, state):
#         return [state + self.delta, state - self.delta]

#     def result(self, stateIgnored, x):
#         return x

#     def value(self, x):
#         return math.fabs(x * math.sin(x))
#         # Thought about limiting the problem size but decided against it
#         # if 0 <= x <= 30:
#         #     return math.fabs(x * math.sin(x))
#         # else:
#        #     return 0


if __name__ == '__main__':

    # Formulate a problem with a 2D hill function and a single maximum value.
    fillInSize = citySize = 10
    maximum = citySize
    cityConfig = [[0 for x in range(citySize)] for y in range(citySize)]
    for i in range(citySize):
        fillInSize -= 1
        for j in range(fillInSize):
            cityConfig[i + j + 1][i] = cityConfig[i][i +
                                                     j + 1] = randrange(1, 10, 1)

    print(cityConfig)

    # For loop to do find solutions to random starting variables
    # for count in range(restartTimes):
    #     initial = randrange(0, maximum)
    #     time1 = time.time()
    #     p = AbsVariant(initial, maximum, delta=1)
    #     time2 = time.time()
    #     totalValInit += p.value(initial)
    #     timeForInit += (time2 - time1)
    #     if maxValInit < p.value(initial):
    #         maxValInit = p.value(initial)

    #     # Solve the problem using hill-climbing.
    #     time1 = time.time()
    #     hill_solution = hill_climbing(p)
    #     time2 = time.time()
    #     totalValHill += p.value(hill_solution)
    #     timeForHill += (time2 - time1)
    #     if maxValHill < p.value(hill_solution):
    #         maxValHill = p.value(hill_solution)

    #     # Solve the problem using simulated annealing.
    #     time1 = time.time()
    #     annealing_solution = simulated_annealing(
    #         p,
    #         exp_schedule(k=20, lam=0.005, limit=1000)
    #     )
    #     time2 = time.time()
    #     totalValAnneal += p.value(annealing_solution)
    #     timeForAnneal += (time2 - time1)
    #     if maxValAnneal < p.value(annealing_solution):
    #         maxValAnneal = p.value(annealing_solution)
