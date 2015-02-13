#!/usr/bin/env python

"""Client code for HW 2 (Genetic Programming)."""

import random

from expression_tree import ExprTree
import genetic

__author__ = "Ben Wiley and Jackson Spell"
__email__ = "bewiley@davidson.edu, jaspell@davidson.edu"

def main():

	pop_size = 10
	max_runs = 50

	# Which data set to use.
	mode = 1

	random.seed()

	pop = []

	# Create a random population of trees.
	for i in range(pop_size):
		pop.append(ExprTree(mode))

	print "Population created."
	for tree in pop:
		print tree

	for i in range(max_runs):

		print "Beginning crossover " + str(i) + ":"

		# Crossover and mutate population.
		pop = genetic.crossover(pop, mode)

		print "Crossover " + str(i) + " complete."

		for tree in pop:
			print tree


if __name__ == "__main__":
	main()