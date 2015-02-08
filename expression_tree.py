"""Expression Tree object for HW 2 (Genetic Programming)."""

import math

__author__ = "Ben Wiley and Jackson Spell"
__email__ = "bewiley@davidson.edu, jaspell@davidson.edu"

class ExprTree:
	"""
	A tree representing a mathematical expression.
	"""

	def __init__(self, ops):
		"""
		ExprTree Constructor.

		Parameters:
			ops - bool - complex operations allowed (e^x, sin, log)

		Returns:
			randomly built expression tree
		"""

		# Use all operations
		if ops:

		# Use only +, -, *, /, pow.		
		else:


	def evaluate(self, x):
		"""
		Evaluate the expression tree and return the result.

		Parameters:
			x - float - input variable

		Returns:
			float - value the tree evaluates to
		"""

		return float(ExprTree.evaluate(self.root, x))

	@staticmethod
	def evaluate(node, x):
		"""
		Evaluate the node and return the result.

		Static method.

		Parameters:
			node - Node - node to evaluate
			x - float - input variable

		Returns:
			int or float - value the node evaluates to
		"""

		if node.value == "x":
			return x
		elif type(node.value) is int:
			return node.value

		elif node.value == "+":
			return ExprTree.evaluate(node.left, x) + ExprTree.evaluate(node.right, x)
		elif node.value == "-":	
			return ExprTree.evaluate(node.left, x) - ExprTree.evaluate(node.right, x)
		elif node.value == "*":
			return ExprTree.evaluate(node.left, x) * ExprTree.evaluate(node.right, x)
		elif node.value == "/":
			return ExprTree.evaluate(node.left, x) / float(ExprTree.evaluate(node.right, x))
		elif node.value == "pow":
			return math.pow(x, ExprTree.evaluate(node.left, x))

		elif node.value == "e":
			return math.exp(ExprTree.evaluate(node.left, x))
		elif node.value == "sin":
			return math.sin(ExprTree.evaluate(node.left, x))
		elif node.value == "log":
			return math.log(ExprTree.evaluate(node.left, x))

	@staticmethod
	def combine(first, second):
		"""
		Combine 2 trees to create a child tree.

		Static method.

		Parameters:
			first - ExprTree - tree to combine
			second - ExprTree - tree to combine

		Returns:
			ExprTree - child of given trees
		"""

		pass

	class Node:
		"""
		Node for ExprTree.
		"""

		def __init__(self, v):
			"""
			Node Constructor.

			Parameters:
				v - int, string - value of node (either int or +, -, *, /, pow, e, sin, log)

			Returns:
				instantiated node with given value and empty children
			"""

			if type(v) is int or v in ("+", "-", "*", "/", "pow", "e", "sin", "log"):
				self.value = v
				self.left = None
				self.right = None

			else:
				raise ValueError("incorrect node value: " + str(v))

