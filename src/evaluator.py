from nodes import *
from values import Number

class Evaluator:

	def __init__(self, tree):
		self.tree = tree

	def evaluate(self):
		return self.eval(self.tree)

	def eval(self, tree):
		method_name = f"eval_{type(tree).__name__}"
		method = getattr(self, method_name)
		return method(tree)

	def eval_NumberNode(self, node):
		return Number(node.value)

	def eval_AddNode(self, node):
		return Number(self.eval(node.node_x).value + self.eval(node.node_y).value)

	def eval_SubtractNode(self, node):
		return Number(self.eval(node.node_x).value - self.eval(node.node_y).value)

	def eval_MultiplyNode(self, node):
		return Number(self.eval(node.node_x).value * self.eval(node.node_y).value)

	def eval_DivideNode(self, node):
		try:
			return Number(self.eval(node.node_x).value / self.eval(node.node_y).value)
		except:
			raise Exception("Runtime math error")

	def eval_PlusNode(self, node):
		return Number(self.eval(node.node).value)

	def eval_MinusNode(self, node):
		return Number(-1 * self.eval(node.node).value)
