from dataclasses import dataclass

@dataclass
class NumberNode:
	value: float

	def __repr__(self):
		return f"{self.value}"

@dataclass
class AddNode:
	node_x: any
	node_y: any

	def __repr__(self):
		return f"({self.node_x} + {self.node_y})"

@dataclass
class SubtractNode:
	node_x: any
	node_y: any

	def __repr__(self):
		return f"({self.node_x} - {self.node_y})"

@dataclass
class MultiplyNode:
	node_x: any
	node_y: any

	def __repr__(self):
		return f"({self.node_x} * {self.node_y})"

@dataclass
class DivideNode:
	node_x: any
	node_y: any

	def __repr__(self):
		return f"({self.node_x} / {self.node_y})"

@dataclass
class PlusNode:
	node: any

	def __repr__(self):
		return f"(+{self.node})"

@dataclass
class MinusNode:
	node: any

	def __repr__(self):
		return f"(-{self.node})"











