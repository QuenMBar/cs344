"""
This module implements local search on the Traveling Salesman Problem.  It uses
simulated annealing and hill climbing to do this.  It will randomly create a city
that has a list of linked cities in it.  It will then use the above algorithms to
try and find the shortest path through them.

@author: Quentin Barnes
"""
import math
import time
from search import Problem, hill_climbing, simulated_annealing, \
    exp_schedule, genetic_search
from random import randrange, shuffle


class TPSVariant(Problem):
    """
    State: Current order of citys
    Action: Take the city with the longest distance to the next one, then make a list
    of all the other cities swaped with that one.
    Value: Total distance took to travel between the cities
    """

    # Sets the initial state, the size of the city, the configuration of the cities, and the maximum distance
    def __init__(self, initial, citySize, cityConfig, maximum, connectHome):
        self.initial = initial[:]
        self.citySize = citySize
        self.cityConfig = cityConfig
        self.maximum = maximum
        self.connectHome = connectHome

    # It takes the city with the max distance to the next one and then
    # makes a list of that city swaped with each other city as the actions
    def actions(self, state):
        max = self.getMaxDistNode(state)
        options = []
        for i in range(self.citySize):
            if i != max:
                newOption = state[:]
                newOption[i], newOption[max] = newOption[max], newOption[i]
                options.append(newOption[:])
        return options[:]

    # Result is the action taken
    def result(self, state, action):
        return action[:]

    # Inverts the realValue since the algorithms are looking for a maximum,
    # while we are looking for the minimum distance
    def value(self, state):
        return self.maximum - self.realValue(state)

    # Uses the city configuration to sum up the total distance that the salesman travels
    def realValue(self, state):
        totalDist = 0
        for i in range(self.citySize - 1):
            totalDist += self.cityConfig[state[i]][state[i + 1]]
        if self.connectHome:
            totalDist += self.cityConfig[self.citySize-1][1]
        return totalDist

    # Finds and returns the index of the node with the max distance
    def getMaxDistNode(self, state):
        indexOfMax = 0
        lengthOfMax = 0
        for n in range(self.citySize - 1):
            if self.cityConfig[state[n]][state[n + 1]] > lengthOfMax:
                indexOfMax = n
                lengthOfMax = self.cityConfig[state[n]][state[n + 1]]
        return indexOfMax


if __name__ == '__main__':

    # Sets the values of how large the city is and the max distance between them
    # Also sets if the problem should be a loop or not
    fillInSize = citySize = 30
    maxDistance = 20
    connectHome = False

    # Creates the city configuration
    maximum = citySize * maxDistance
    cityConfig = [[0 for x in range(citySize)] for y in range(citySize)]
    for i in range(citySize):
        fillInSize -= 1
        for j in range(fillInSize):
            cityConfig[i + j + 1][i] = cityConfig[i][i +
                                                     j + 1] = randrange(1, maxDistance, 1)

    # Creates an initial state
    totalHill = 0
    totalSim = 0
    for i in range(100):
        initial = [x for x in range(citySize)]
        shuffle(initial)

        p = TPSVariant(initial, citySize, cityConfig, maximum, connectHome)

        time1 = time.time()
        hill_solution = hill_climbing(p)
        time2 = time.time()

        simAneal = simulated_annealing(
            p,
            exp_schedule(k=20, lam=0.005, limit=1000)
        )
        time3 = time.time()
        totalHill += p.realValue(hill_solution)
        totalSim += p.realValue(simAneal)

    print(totalHill / 100)
    print(totalSim/100)

    print("Initial: \t\t\t\t\t", initial, "  Distance: ", p.realValue(initial))
    print("Hill Climbing solution: \t", hill_solution,
          "  Distance: ", p.realValue(hill_solution), "  Time: ", (time2 - time1))
    print("Sim Anneal solution: \t\t", simAneal,
          "  Distance: ", p.realValue(simAneal), "  Time: ", (time3 - time2))
