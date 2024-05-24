from lexer import Lexer
from parse import Parser
from interpreter import Interpreter


while True:
    text = input("Cosmos: ")

    tokenizer = Lexer(text)
    tokens = tokenizer.tokenize()

    print(tokens)

    parser = Parser(tokens)
    tree = parser.parse()

    print(tree)

    # interpreter = Interpreter(tree)
    # result = interpreter.interpret()

    # print(result)