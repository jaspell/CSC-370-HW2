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

