"""Expression Tree object for HW 2 (Genetic Programming)."""

import math
import random

__author__ = "Ben Wiley and Jackson Spell"
__email__ = "bewiley@davidson.edu, jaspell@davidson.edu"

class ExprTree:
	"""
	A tree representing a mathematical expression.
	"""

	OPS_1 = ["x", "+", "-", "*", "/"]
	OPS_2 = ["x", "x2", "x3", "+", "-", "*", "/"]
	OPS_3 = ["x", "+", "-", "*", "/", "e", "sin", "log"]

	OPS_VARS = ["x", "x2", "x3"]
	OPS_UNARY = ["e", "sin", "log"]
	OPS_BINARY = ["+", "-", "*", "/"]

	def __init__(self, ops, original=None):
		"""
		ExprTree Constructor.

		Parameters:
			ops - int - 1 for simple ops, 2 for three-var (x1, x2, x3),
				3 for complex operations allowed (e^x, sin, log)
			original - ExprTree - tree to copy

		Returns:
			randomly built expression tree
		"""

		if original:
			self.root = Node(original.root.value)
			clone(self.root, original.root.left, original.root.right)

		# Use only x, +, -, *, /,.
		elif ops == 1:

		# Use only x1, x2, x3, +, -, *, /.		
		elif ops == 2:

		# Use one variable with all available operations.
		else: # ops == 3:
			

	def count(self):
		"""
		Recursive function for counting number of nodes in tree.

		Parameters:
			none

		Returns:
			int - number of nodes
		"""

		return count(self.root)


	@staticmethod
	def count(node):
		"""
		Recursive function for counting number of nodes rooted at given node.

		Parameters:
			node - Node - the root node

		Returns:
			int - number of nodes
		"""

		c = 1
		if node.left:
			c += count(node.left)
		if node.right:
			c += count(node.right)
		return c

	def random_parent(self):
		"""
		Finds a random non-root node in tree and returns its parent and direction (left/right)

		Parameters:
			none

		Returns:
			tuple - (parent, left)
				parent - Node - parent of the chosen node
				left - bool - indicates whether chosen node is the left child of the parent
		"""

		c = count()
		r = random.randint(2, c)
		parent, left, count, found = get_parent(self.root, r)
		return parent, left

	@staticmethod
	def get_parent(node, n, count=0):
		"""
		Recursive function to find nth node in tree depth-first, return its parent and [left/right].

		Parameters:
			node - Node - the current node
			n - int - which node to search for
			count - int - # of nodes that have been searched before this node

		Returns:
			tuple - (parent, left, count, found)
				parent - Node - parent of the found node (will be passed as None unless found)
				left - bool - indicates whether found node is left child of parent (None unless found)
				count - int - total # of nodes that have been searched after subtree is exhausted
				found - bool - indicates whether desired node has been found
		"""

		count += 1

		if count == n:
			return None, None, count, True

		if node.left:

			parent, left, count, found = get_parent(node.left, n, count)

			if found:

				if parent:
					return parent, left, count, found
				else:
					return node, True, count, found

		if node.right:

			parent, left, count, found = get_parent(node.right, n, count)

			if found:

				if parent:
					return parent, left, count, found
				else:
					return node, False, count, found

		return None, None, count, False

	@staticmethod
	def clone(node, left=None, right=None):
		"""
		Recursive function to clone the left and right nodes for corresponding
			fields in the given new node.

		Parameters:
			node - Node - the current (already cloned) node
			left - Node - the previous left node to be cloned
			right - Node - the previous right node to be cloned

		Returns:
			nothing
		"""

		if left:

			node.left = Node(left.value)
			clone(node.left, left.left, left.right)

		if right:

			node.right = Node(right.value)
			clone(node.right, right.left, right.right)

	def evaluate(self, x, x2=None, x3=None):
		"""
		Evaluate the expression tree and return the result.

		Parameters:
			x, x2, x3 - float - input variables

		Returns:
			float - value the tree evaluates to
		"""

		return float(ExprTree.evaluate(self.root, x, x2, x3))

	@staticmethod
	def evaluate(node, x, x2, x3):
		"""
		Evaluate the node and return the result.

		Static method.

		Parameters:
			node - Node - node to evaluate
			x, x2, x3 - float - input variables

		Returns:
			int or float - value the node evaluates to
		"""

		# Vars and Constants
		if node.value == "x":
			return x
		elif node.value == "x2":
			return x2
		elif node.value == "x3":
			return x3
		elif type(node.value) is int or type(node.value) is float:
			return node.value

		# Binary Ops
		elif node.value == "+":
			return ExprTree.evaluate(node.left,x,x2,x3) + ExprTree.evaluate(node.right,x,x2,x3)
		elif node.value == "-":	
			return ExprTree.evaluate(node.left,x,x2,x3) - ExprTree.evaluate(node.right,x,x2,x3)
		elif node.value == "*":
			return ExprTree.evaluate(node.left,x,x2,x3) * ExprTree.evaluate(node.right,x,x2,x3)
		elif node.value == "/":
			return ExprTree.evaluate(node.left,x,x2,x3) / float(ExprTree.evaluate(node.right,x,x2,x3))

		# Unary Ops on X
		elif node.value == "e":
			return math.exp(x)
		elif node.value == "sin":
			return math.sin(x)
		elif node.value == "log":
			return math.log(x)

	"""
	@staticmethod
	def combine(first, second):
		"#""
		Combine 2 trees to create a child tree.

		Static method.

		Parameters:
			first - ExprTree - tree to combine
			second - ExprTree - tree to combine

		Returns:
			ExprTree - child of given trees
		"#""

		pass
	"""

	def __str__(self):
		"""
		Return a readable representation of the tree's equivalent function

		Parameters:
			none

		Returns:
			string - human-readable representation of the tree's equivalent function
		"""

		return str(self.root)

	class Node:
		"""
		Node for ExprTree.
		"""

		def __init__(self, v):
			"""
			Node Constructor.

			Parameters:
				v - int, string - value of node (int, float or x, +, -, *, /, e, sin, log)

			Returns:
				instantiated node with given value and empty children
			"""

			self.value = v
			self.left = None
			self.right = None

		def __str__(self):
			"""
			Return a readable representation of the equivalent function of tree rooted at node

			Parameters:
				none

			Returns:
				string - readable representation of the equivalent function of tree rooted at node
			"""

			# Vars and Constants
			if self.value == "x" or self.value == "x2" or self.value == "x3":
				return self.value
			elif type(self.value) is int or type(self.value) is float:
				return str(self.value)

			# Binary Ops
			elif self.value == "+" or self.value == "-" or self.value == "*" or self.value == "/":
				return "(" + str(self.left) + self.value + str(self.right) + ")"

			# CHANGE FOR ACTUAL GENERATOR 3 IMPLEMENTATION
			# Unary Ops on X
			elif self.value == "e":
				return "e^x"
			elif self.value == "sin":
				return "sin(x)"
			elif self.value == "log":
				return "log(x)"

