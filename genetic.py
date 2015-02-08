"""Genetic programming algorithm for HW 2 (8-puzzle A* search)."""

from expression_tree import ExprTree

__author__ = "Ben Wiley and Jackson Spell"
__email__ = "bewiley@davidson.edu, jaspell@davidson.edu"

"""
We should include the fitness functions in here, which will use a squared error evaluation.
"""

def fitness(tree):
	"""
	Evaluate the fitness of a given tree using squared error.

	Parameters:
		tree - ExprTree - tree to evaluate

	Returns:
		float - fitness of tree, smaller is better
	"""

def crossover(pop):
	"""
	Create new generation from current population.

	Parameters:
		pop - list of ExprTree's - parent population

	Returns:
		list of ExprTree's - new population
	"""