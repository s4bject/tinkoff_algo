def operation(operator,operand1,operand2):
    if operator == "+":
        return operand1 + operand2
    elif operator == "-":
        return operand1 - operand2
    elif operator == "*":
        return operand1 * operand2


def postfix(arr):
    stack = []

    for oper in arr:
        if oper.isdigit() or (oper[0] == "-" and oper[1:].isdigit()):
            stack.append(int(oper))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = operation(oper,operand1,operand2)
            stack.append(result)
    return stack.pop()



postfix_note = input().split()
print(postfix(postfix_note))