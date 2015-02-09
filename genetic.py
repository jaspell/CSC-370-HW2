"""Genetic programming algorithm for HW 2 (8-puzzle A* search)."""

import os

from expression_tree import ExprTree

__author__ = "Ben Wiley and Jackson Spell"
__email__ = "bewiley@davidson.edu, jaspell@davidson.edu"

"""
We should include the fitness functions in here, which will use a squared error evaluation.
"""

def fitness(tree, mode):
	"""
	Evaluate the fitness of a given tree using squared error.

	Parameters:
		tree - ExprTree - tree to evaluate
		mode - int - 1, 2, 3 - which data source this run uses

	Returns:
		float - fitness of tree, smaller is better
	"""

	# Test vs holdout ratio of data in data.txt.
	ratio = 0.8
	total_data = 100000

	# Step size for input variable.
	step = 0.05
	num_points = 100
	
	error = 0.0

	# Evaluate fitness based on Generator1.jar.
	if mode == 1:
		for x in range(num_points):
			error += (tree.evaluate(x*step) - os.system("java -jar Generator1.jar "+str(x*step)))**2

	# Evaluate fitness based on data.txt.
	elif mode == 2:
		with open("data.txt", 'r') as inf:
			for i in range(ratio*total_data):
				inputs = inf.next().split()
				error += (tree.evaluate(inputs[0], inputs[1], inputs[2]) - inputs[3])**2

	# Evaluate fitness based on Generator2.jar.
	elif mode == 3:
		for x in range(num_points):
			error += (tree.evaluate(x*step) - os.system("java -jar Generator2.jar "+str(x*step)))**2

	return error

def crossover(pop):
	"""
	Create new generation from current population.

	Parameters:
		pop - list of ExprTree's - parent population

	Returns:
		list of ExprTree's - new population
	"""


def mutate(pop, ratio):
	"""
	Alter population by mutation.

	Parameters:
		pop - list of ExprTree's - original population
		ratio - float - 0.0 <= ratio < 1.0 - proportion of population to mutate

	Returns:
		list of ExprTree's - mutated population
	"""