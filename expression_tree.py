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
		Fix this doc later
		"""

		def __init__(self, original=None):
			"""
			Node Constructor.

			Parameters:
				original - Node - node to copy

			Returns:
				instantiated copy of the original node (if supplied),
				or otherwise, a node with no defined properties
				(I MIGHT WANT TO CHANGE THIS)
			"""

			if original is None:


			else:
				#set all properties to equal those of original

				self.left = Node(original.left)
				self.right = Node(original.right)



