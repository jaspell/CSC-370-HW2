"""Genetic programming algorithm for HW 2 (8-puzzle A* search)."""

import os
import sys
import random

import numpy

from expression_tree import ExprTree

__author__ = "Ben Wiley and Jackson Spell"
__email__ = "bewiley@davidson.edu, jaspell@davidson.edu"

def fitness(tree, mode):
	"""
	Evaluate the fitness of a given tree using squared error.

	Parameters:
		tree - ExprTree - tree to evaluate
		mode - int - 1, 2, 3 - which data source to evaluate the tree on

	Returns:
		float - fitness of tree, smaller is better
	"""

	# Test vs holdout ratio of data in data.txt.
	ratio = 0.8
	total_data = 100000

	# Step size for input variable.
	step = 0.05
	num_points = 100
	
	
	# Maximum number of nodes the tree is allowed to have.
	max_size = 16

	# If tree exceeds max size, it's no good.
	if tree.count() > max_size:
		return sys.maxint

	# Error is initialized to 0.000001 to avoid divide-by-zero errors.
	error = 0.000001

	try:
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

	# If the tree causes a ValueError, it's no good.
	except ValueError:
		return sys.maxint

	return error

def crossover(pop, mode):
	"""
	Create new generation from current population.

	Parameters:
		pop - list of ExprTree's - parent population
		mode - int - 1, 2, 3 - which data source to evaluate the trees on

	Returns:
		list of ExprTrees - child population of same size as input population
	"""

	# Evaluate each tree's fitness.  Crossover weights are the inverse of the fitness score.
	fit = []
	for tree in pop:
			fit.append(1.0 / fitness(tree, mode))

	crosses = weighted_pick(fit, len(fit))
	children = []

	for i in xrange(0, len(crosses), 2):
		c1, c2 = ExprTree.combine(pop[crosses[i]], pop[crosses[i+1]])
		children.append(c1)
		children.append(c2)

	return children

def weighted_pick(weights,n_picks):
	"""
	Weighted random selection from a list.

	Sourced from http://glowingpython.blogspot.com/2012/09/weighted-random-choice.html.

	Parameters:
		weights - list of floats - list of weighting factors for tree choices
		n_picks - int - number of indexes to pick

	Returns:
		list of indices
	"""

	t = numpy.cumsum(weights)
	s = sum(weights)
	return numpy.searchsorted(t,numpy.random.rand(n_picks)*s)

def mutate(pop, ratio, mode):
	"""
	Alter population by mutation.

	Parameters:
		pop - list of ExprTree's - original population
		ratio - float - 0.0 <= ratio < 1.0 - proportion of population to mutate
		mode - int - 1, 2, 3 - which data source to evaluate the trees on

	Returns:
		None
	"""

	for tree in pop:
		if random.random() < ratio:
			mutate(tree)

def mutate(tree, mode):
	"""
	Mutate given tree at one node.

	Parameters:
		tree - ExprTree - tree to mutate
		mode - int - 1, 2, 3 - which data source to evaluate the trees on

	Returns:
		None
	"""

	# CHANGE RANDINT BOUNDS DEPENDING ON INDEXING SYSTEM FOR NODE COUNTING (DFS SEARCH, COUNT).
	node = tree.find_node(random.randint(0, tree.count()))
	mutate_node(node, mode)

def mutate_node(node, mode):
	"""
	Mutate node.

	Parameters:
		node - ExprTree.Node - original node to mutate
		mode - int - 1, 2, 3 - which data source to evaluate the trees on

	Returns:
		None
	"""

	# Replace node.value with either input variable or constant.
	if type(node.value) is int or node.value in ExprTree.OPS_VARS:

	# Replace node.value with a unary operator.
	elif node.value in ExprTree.OPS_UNARY:

	# Replace node.value with a binary operator.
	elif node.value in ExprTree.OPS_BINARY: