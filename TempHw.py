"""
This uses a pre-built problem specification for the
Zebra puzzle taken from AIMA's csp.py. See:

    https://en.wikipedia.org/wiki/Zebra_Puzzle

@author: kvlinden
@version 14feb2013
"""
import time

from csp import min_conflicts, backtracking_search, AC3, CSP, parse_neighbors
from search import depth_first_graph_search


def print_solution(result):
    """A CSP solution printer copied from csp.py."""
    for h in range(1, 6):
        print('House', h)
        for (var, val) in result.items():
            if val == h:
                print('\t', var)


def Zebra():
    """Return an instance of the Zebra Puzzle."""
    Rooms = 'GoldLab RedLab'.split()
    Teachers = 'Schuurman Adams Norman VanderLinden'.split()
    Classes = 'CS108 CS112 CS212 CS214 CS344 CS300 CS384'.split()
    variables = Rooms + Teachers + Classes
    domains = {}
    for var in variables:
        domains[var] = ['MWF800', 'MWF900', 'MWF1030', 'TTH1030', 'TTH1200']
    neighbors = parse_neighbors("""Schuurman: CS300;
                Schuurman: CS384; VanderLinden: CS344; VanderLinden: CS108;
                Norman: CS214; Adams: CS212; Adams: CS112""", variables)
    for type in [Rooms, Teachers, Classes]:
        for A in type:
            for B in type:
                if A != B:
                    if B not in neighbors[A]:
                        neighbors[A].append(B)
                    if A not in neighbors[B]:
                        neighbors[B].append(A)
    print(neighbors)
    print(domains)

    def zebra_constraint(A, a, B, b, recurse=0):
        return a == b
        # same = (a == b)
        # if A == 'Englishman' and B == 'Red':
        #     return same
        # if A == 'Spaniard' and B == 'Dog':
        #     return same
        # if A == 'Chesterfields' and B == 'Fox':
        #     return next_to
        # if A == 'Norwegian' and B == 'Blue':
        #     return next_to
        # if A == 'Kools' and B == 'Yellow':
        #     return same
        # if A == 'Winston' and B == 'Snails':
        #     return same
        # if A == 'LuckyStrike' and B == 'OJ':
        #     return same
        # if A == 'Ukranian' and B == 'Tea':
        #     return same
        # if A == 'Japanese' and B == 'Parliaments':
        #     return same
        # if A == 'Kools' and B == 'Horse':
        #     return next_to
        # if A == 'Coffee' and B == 'Green':
        #     return same
        # if A == 'Green' and B == 'Ivory':
        #     return a - 1 == b
        # if recurse == 0:
        #     return zebra_constraint(B, b, A, a, 1)
        # if ((A in Colors and B in Colors) or
        #         (A in Pets and B in Pets) or
        #         (A in Drinks and B in Drinks) or
        #         (A in Countries and B in Countries) or
        #         (A in Smokes and B in Smokes)):
        #     return not same
        # raise Exception('error')
    return CSP(variables, domains, neighbors, zebra_constraint)


puzzle = Zebra()

# result = depth_first_graph_search(puzzle)
# result = AC3(puzzle)
result = backtracking_search(puzzle)
# result = min_conflicts(puzzle, max_steps=1000)

if puzzle.goal_test(puzzle.infer_assignment()):
    print("Solution:\n")
    print_solution(result)
else:
    print("failed...")
    print(puzzle.curr_domains)
    puzzle.display(puzzle.infer_assignment())
