operators = ("+", "-", "*", "/")

tokens = ["2", "1", "+", "3", "*"]

stack = []
for token in tokens:
    if token not in operators:
        stack.append(int(token))
    else:
        a = stack.pop()
        b = stack.pop()
        if token == "+":
            result = b + a
        if token == "-":
            result = b - a
        if token == "*":
            result = b * a
        if token == "/":
            result = b / a
        stack.append(int(result))

print(stack.pop())
