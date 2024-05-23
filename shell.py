from lexer import Lexer

while True:
    text = input("Cosmos: ")
    tokenizer = Lexer(text)
    tokens = tokenizer.tokenize()

    print(tokens)