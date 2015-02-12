"""Expression Tree object for HW 2 (Genetic Programming)."""

import math

__author__ = "Ben Wiley and Jackson Spell"
__email__ = "bewiley@davidson.edu, jaspell@davidson.edu"

class ExprTree:
	"""
	A tree representing a mathematical expression.
	"""

	OPS_1 = ["x", "+", "-", "*", "/", "pow"]
	OPS_2 = ["x", "x2", "x3", "+", "-", "*", "/", "pow", "pow2", "pow3"]
	OPS_3 = ["x", "+", "-", "*", "/", "pow", "e", "sin", "log"]

	OPS_VARS = ["x", "x2", "x3"]
	OPS_UNARY = ["e", "sin", "log", "pow", "pow2", "pow3"]
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

		# Use only x, +, -, *, /, pow.
		elif ops == 1:

		# Use only x1, x2, x3, +, -, *, /, pow.		
		elif ops == 2:

		# Use one variable with all available operations.
		else: # ops == 3:
			

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

		# Integer Powers of X1, X2 and X3
		elif node.value == "pow":
			return math.pow(x, node.power)
		elif node.value == "pow2":
			return math.pow(x2, node.power)
		elif node.value == "pow3":
			return math.pow(x3, node.power)

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

		return to_string(self.root)

	@staticmethod
	def to_string(node):
		"""
		Return a readable representation of the equivalent function of tree rooted at node

		Parameters:
			node - Node - root of tree to evaluate

		Returns:
			string - human-readable representation of the equivalent function of tree rooted at node
		"""

		# Vars and Constants
		if node.value == "x" or node.value == "x2" or node.value == "x3":
			return value
		elif type(node.value) is int or type(node.value) is float:
			return str(node.value)

		# Binary Ops
		elif node.value == "+" or node.value == "-" or node.value == "*" or node.value == "/":
			return "(" + to_string(node.left) + node.value + to_string(node.right) + ")"

		# Integer Powers of X1, X2 and X3
		elif node.value == "pow":
			return "x^" +  str(node.power)
		elif node.value == "pow2":
			return "x2^" +  str(node.power)
		elif node.value == "pow3":
			return "x3^" +  str(node.power)

		# Unary Ops on X
		elif node.value == "e":
			return "e^x"
		elif node.value == "sin":
			return "sin(x)"
		elif node.value == "log":
			return "log(x)"

	class Node:
		"""
		Node for ExprTree.
		"""

		def __init__(self, v, p=None):
			"""
			Node Constructor.

			Parameters:
				v - int, string - value of node (int, float or x,+,-,*,/,pow,pow2,pow3,e,sin,log)

			Returns:
				instantiated node with given value and empty children
			"""

			self.value = v
			self.left = None
			self.right = None
			if p: self.power = p

