'''
from infixToPostfix import infixToPostfix
from postfixEval import postfixEval

def infixEval(infix):
    return postfixEval(infixToPostfix(s))

'''
from Stack_ori import Stack
def infixEval(infix):
    opndStack = Stack()

    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    optrStack = Stack()

    infix_ava = ' '.join(infix)
    tokenList = infix_ava.split()

    for token in tokenList:
        if token in '0123456789':
            opndStack.push(int(token))
        elif token == '(':
            optrStack.push(token)
        elif token == ')':
            topToken = optrStack.pop()
            while topToken != '(':
                cal(opndStack, topToken)
                topToken = optrStack.pop()
        elif (not optrStack.isEmpty()) and (prec[optrStack.peek()] >= prec[token]):
            cal(opndStack, token)
        else:
            optrStack.push(token)

    while not optrStack.isEmpty():
        cal(opndStack, optrStack.pop())
    return opndStack.pop()


def cal(stack, op):
    operand1 = stack.pop()
    operand2 = stack.pop()
    result = doMath(op, operand1, operand2)
    stack.push(result)


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


s = input("请输入一个中序表达式：")
print(infixEval(s))



