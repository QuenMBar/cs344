'''
This module implements the Bayesian network shown in the text, Figure 14.2.
It's taken from the AIMA Python code.

@author: kvlinden
@edited: Quentin Barnes
@version Jan 2, 2013
'''

from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask

# Utility variables
T, F = True, False

# Cancer example from lab 5-Cs 344
cancer = BayesNet([
    ('Cancer', '', 0.01),
    ('Test1', 'Cancer', {T: 0.90, F: 0.20}),
    ('Test2', 'Cancer', {T: 0.90, F: 0.20})
])

print('P(Cancer | positive results on both tests): ')
print(enumeration_ask('Cancer', dict(
    Test1=T, Test2=T), cancer).show_approx())

print('\nP(Cancer | a positive result on test 1, but a negative result on test 2): ')
print(enumeration_ask('Cancer', dict(
    Test1=T, Test2=F), cancer).show_approx())
