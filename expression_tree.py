"""Expression Tree object for HW 2 (Genetic Programming)."""

import math

__author__ = "Ben Wiley and Jackson Spell"
__email__ = "bewiley@davidson.edu, jaspell@davidson.edu"

class ExprTree:
	"""
	A tree representing a mathematical expression.
	"""

	def __init__(self, original=None):
		"""
		ExprTree Constructor.

		Parameters:
			original - ExprTree - tree to copy

		Returns:
			instantiated copy of the original board (if supplied),
			or otherwise, randomly built expression tree
		"""

		if original is None:


		else:
			self.root = original.root.clone()

	def evaluate(self, x):
		"""
		Evaluate the expression tree and return the result.

		Parameters:
			x - float - input variable

		Returns:
			float - value the tree evaluates to
		"""

		return float(evaluate(root, x))

	def evaluate(self, node, x):
		"""
		Evaluate the node and return the result.

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
			return evaluate(node.left) + evaluate(node.right)
		elif node.value == "-":	
			return evaluate(node.left) - evaluate(node.right)
		elif node.value == "*":
			return evaluate(node.left) * evaluate(node.right)
		elif node.value == "/":
			return evaluate(node.left) / float(evaluate(node.right))

		elif node.value == "pow":
			return math.pow(x, evaluate(node.left))
		elif node.value == "e":
			return math.exp(evaluate(node.left))
		elif node.value == "sin":
			return math.sin(evaluate(node.left))
		elif node.value == "log":
			return math.log(evaluate(node.left))

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

