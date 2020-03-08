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

# From lab 05 - Cs 344
burglary = BayesNet([
    ('Sunny', '', 0.70),
    ('Raise', '', 0.01),
    ('Happy', 'Sunny Raise', {
        (T, T): 1.0, (T, F): 0.7, (F, T): 0.9, (F, F): 0.1})
])

print('P(Raise | sunny): ')
print(enumeration_ask('Raise', dict(
    Sunny=T), burglary).show_approx())

print('\nP(Raise | happy ∧ sunny): ')
print(enumeration_ask('Raise', dict(
    Happy=T, Sunny=T), burglary).show_approx())

print('\nP(Raise | happy): ')
print(enumeration_ask('Raise', dict(
    Happy=T), burglary).show_approx())

print('\nP(Raise | happy ∧ ¬sunny): ')
print(enumeration_ask('Raise', dict(
    Happy=T, Sunny=F), burglary).show_approx())
