from lexer import Lexer
from parser_ import Parser
from evaluator import Evaluator

while True:
	try:
		text = input(">>> ")
		lexer = Lexer(text)
		tokens = lexer.generate_tokens()
		# print(list(tokens))
		parser = Parser(tokens)
		tree = parser.parse()
		# print(tree)
		evaluate = Evaluator(tree)
		value = evaluate.evaluate()
		print(value)
	except Exception as e:
		print(e)