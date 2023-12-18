expr = input("Insert an expression: ")
print("The result is:", eval(expr)) if eval(expr) >= 0 else print("The result is:", -eval(expr))
