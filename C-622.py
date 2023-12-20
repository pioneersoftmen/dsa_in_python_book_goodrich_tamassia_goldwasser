def evaluate_postfix(expression):
    S = [] # Stack to store operands

    for element in expression.split():
        if element.isdigit(): # Check if the element is an operand
            S.append(int(element)) # Convert and push to the stack
        else:
            operand2 = S.pop() # Pop the top two operands from the stack
            operand1 = S.pop()

            if element == '+': # Perform the corresponding operation
                result = operand1 + operand2
            elif element == '-':
                result = operand1 - operand2
            elif element == '*':
                result = operand1 * operand2
            elif element == '/':
                result = operand1 / operand2

            S.append(result) # Push the result back to the stack

    return S.pop() # Return the final result 

postfix_expression = '5 2 + 8 3 - * 3 /'
result = evaluate_postfix(postfix_expression)
print(result)