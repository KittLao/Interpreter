from tokens import TokenType as tt
from nodes import *

class Parser:

	def __init__(self, tokens):
		self.tokens = iter(tokens)
		self.advance()

	def raise_error(self):
		raise Exception("Invalid syntax")

	def advance(self):
		try:
			self.current_token = next(self.tokens)
		except StopIteration:
			self.current_token = None

	def parse(self):
		if self.current_token == None:
			return None
		result = self.expr()
		"""
		This is caused by invalid syntax sequence of tokens
		that expression rule did not understand.
		"""
		if self.current_token != None:
			self.raise_error()
		return result

	def expr(self):
		"""
		Expr, are all operations and immediates. Want to reduce the operands to terms so
		that all all addition and subtraction operations are on the top of the tree, and
		will be computed last.
		"""
		operand_x = self.term()
		while self.current_token != None and self.current_token.type in (tt.PLUS, tt.MINUS):
			if self.current_token.type == tt.PLUS:
				self.advance() # Skip pass operation token
				operand_y = self.term()
				operand_x = AddNode(operand_x, operand_y)
			elif self.current_token.type == tt.MINUS:
				self.advance() # Skip pass operation token
				operand_y = self.term()
				operand_x = SubtractNode(operand_x, operand_y)
			else:
				break
		return operand_x

	def term(self):
		"""
		Terms are multiplication, division and constants. These operations have the highest
		priority so their trees must be built first and located at the bottom. Their operands
		are constants.
		"""
		operand_x = self.factor()
		while self.current_token != None and self.current_token.type in (tt.MULTIPLY, tt.DIVIDE):
			if self.current_token.type == tt.MULTIPLY:
				self.advance() # Skip pass operation token
				operand_y = self.factor()
				operand_x = MultiplyNode(operand_x, operand_y)
			elif self.current_token.type == tt.DIVIDE:
				self.advance() # Skip pass operation token
				operand_y = self.factor()
				operand_x = DivideNode(operand_x, operand_y)
			else:
				break
		return operand_x

	def factor(self):
		operand = self.current_token
		if operand != None:
			if operand.type == tt.L_PAREN:
				self.advance()
				sub_expr = self.expr() # Build tree for sub-expression in parenthesis
				if self.current_token.type != tt.R_PAREN:
					self.raise_error() # Cannot find closing parenthesis
				self.advance()
				return sub_expr
			elif operand.type == tt.NUMBER:
				return self.terminal()
			elif operand.type == tt.PLUS:
				self.advance()
				return PlusNode(self.terminal())
			elif operand.type == tt.MINUS:
				self.advance()
				return MinusNode(self.terminal())
		"""
		Raise an error if an operator is treated as a factor. Happens when the
		tokens contains consecutive operators, or operators are in wrong palce.
		"""
		self.raise_error()

	def terminal(self):
		operand = self.current_token
		self.advance()
		if operand.type != tt.NUMBER:
			self.raise_error()
		return NumberNode(float(operand.value))



















