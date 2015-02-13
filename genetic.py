"""Genetic programming algorithm for HW 2 (8-puzzle A* search)."""

import subprocess
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
	total_data = 10000

	# Maximum number of nodes the tree is allowed to have.
	max_size = 30

	# If tree exceeds max size, it's no good.
	if tree.count() > max_size:
		return sys.maxint

	# Error is initialized to 0.000001 to avoid divide-by-zero errors (in the perfect case).
	error = 0.000001

	try:
		# Evaluate fitness based on Generator1.jar.
		if mode == 1:
			with open("data_test.txt", 'r') as inf:
				for i in range(int(ratio*total_data)):
					x, y = inf.next().split()
					error += (tree.evaluate_tree(float(x)) - float(y))**2

		# Evaluate fitness based on data.txt.
		elif mode == 2:
			with open("data.txt", 'r') as inf:
				for i in range(int(ratio*total_data)):
					x, x2, x3, y = inf.next().split()
					error += (tree.evaluate_tree(float(x), float(x2), float(x3)) - float(y))**2

		# Evaluate fitness based on Generator2.jar.
		elif mode == 3:
			with open("data2_copy.txt", 'r') as inf:
				for i in range(int(ratio*total_data)):
					x, y = inf.next().split()
					error += (tree.evaluate_tree(float(x)) - float(y))**2

		else:
			raise ValueError("You dun fucked up good, foo!  Wrong mode in fitness")

	# If the tree causes a ValueError, it's no good.
	except (ValueError, ZeroDivisionError):
		return sys.maxint

	return error

def crossover(pop, mode):
	"""
	Create new generation from current population and print best current tree.

	Parameters:
		pop - list of ExprTree's - parent population
		mode - int - 1, 2, 3 - which data source to evaluate the trees on

	Returns:
		list of ExprTrees - child population of same size as input population
	"""

	# Evaluate each tree's fitness.  Crossover weights are the inverse of the fitness score.
	fit = []
	best = (None, sys.maxint)

	for i, tree in enumerate(pop):

		current = fitness(tree, mode)
		if current < best[1]:
			best = (tree, current)

		fit.append(1.0 / current)

		if i % 100 == 0:
			print i

	print "Best tree: " + str(best[0])
	print fit

	crosses = weighted_pick(fit, len(fit))
	print crosses
	children = []

	for i in xrange(0, len(crosses), 2):
		#print "Crossing: " + str(crosses[i]) + " and " + str(crosses[i+1])
		c1, c2 = combine(pop[crosses[i]], pop[crosses[i+1]])
		#print "Result: " + str(c1) + " and " + str(c2)
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

def combine(first, second):
	"""
	Combine 2 trees to create a child tree.

	Static method.

	Parameters:
		first - ExprTree - tree to combine
		second - ExprTree - tree to combine

	Returns:
		tuple - (ExprTree, ExprTree) - children of given trees
	"""

	first = ExprTree(0, first)
	second = ExprTree(0, second)

	parent1, left1 = first.random_parent()
	parent2, left2 = second.random_parent()

	if left1:
		temp = parent1.left

		if left2:
			parent1.left = parent2.left
			parent2.left = temp

		else:
			parent1.left = parent2.right
			parent2.right = temp
	else:
		temp = parent1.right

		if left2:
			parent1.right = parent2.left
			parent2.left = temp

		else:
			parent1.right = parent2.right
			parent2.right = temp

	return first, second

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
		node.value = 5													# CHANGE ME

	# Replace node.value with a unary operator.
	elif node.value in ExprTree.OPS_UNARY:

		# Make sure replacement operation is not the same as the original.
		replace = random.choice(ExprTree.OPS_UNARY)
		while replace == node.value:
			replace = random.choice(ExprTree.OPS_UNARY)

		node.value = replace

	# Replace node.value with a binary operator.
	elif node.value in ExprTree.OPS_BINARY:

		# Make sure replacement operation is not the same as the original.
		replace = random.choice(ExprTree.OPS_BINARY)
		while replace == node.value:
			replace = random.choice(ExprTree.OPS_BINARY)

		node.value = replace