from Stack_ori import Stack


def postfixEval(postfix):
    operandStack = Stack()
    tokenList = postfix.split()#默认空格为分隔符
    for token in tokenList:
        if token in '0123456789':
            operandStack.push(int(token))
        else:
            operand1 = operandStack.pop()
            operand2 = operandStack.pop()
            result = doMath(token, operand1, operand2)
            operandStack.push(result)
    return operandStack.pop()


def doMath(op, op1, op2):
    if op == '+':
        result = op1 + op2
    elif op == '-':
        result = op2 - op1
    elif op == '*':
        result = op1 * op2
    else:
        result = op2 / op1
    return result





