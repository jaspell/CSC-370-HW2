"""Expression Tree object for HW 2 (Genetic Programming)."""

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

	def evaluate(self):
		"""
		Evaluate the expression tree and return the result.

		Parameters:
			None

		Returns:
			int or float - value the tree evaluates to
		"""

		return evaluate(root)

	def evaluate(self, node):
		"""
		Evaluate the node and return the result.

		Parameters:
			node - Node - node to evaluate

		Returns:
			int or float - value the node evaluates to
		"""

		if type(node.value) is int:
			return node.value
		elif node.value == "+":
			return evaluate(node.left) + evaluate(node.right)
		elif node.value == "-":	
			return evaluate(node.left) - evaluate(node.right)
		elif node.value == "*":
			return evaluate(node.left) * evaluate(node.right)
		else:
			return evaluate(node.left) / evaluate(node.right)

	class Node:
		"""
		Node for ExprTree.
		"""

		def __init__(self, v):
			"""
			Node Constructor.

			Parameters:
				v - int, string - value of node (either int or +, -, *, /)

			Returns:
				instantiated node with given value and empty children
			"""

			if type(v) is int or v in ("+", "-", "*", "/"):
				self.value = v
				self.left = None
				self.right = None

			else:
				raise ValueError("incorrect node value: " + str(v))

