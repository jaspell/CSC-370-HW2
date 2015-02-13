#!/usr/bin/env python

"""Client code for HW 2 (Genetic Programming)."""

import random

from expression_tree import ExprTree
#import genetic

__author__ = "Ben Wiley and Jackson Spell"
__email__ = "bewiley@davidson.edu, jaspell@davidson.edu"

def main():

	random.seed()

	e = ExprTree(1)
	print e