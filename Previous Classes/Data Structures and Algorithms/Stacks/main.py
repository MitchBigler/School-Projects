from stack import Stack

#################### EVALUATE POSTFIX ####################
def eval_postfix(expr):
    if type(expr) is not str:
        raise ValueError("eval_postfix - Expression is not a string")
    op_stack = Stack()
    token_list = [x for x in expr]

    if len(token_list) > 0:
        for token in token_list:
            if token == " ":
                continue
            elif token in ["*","/","+","-"]:
                if op_stack.size() < 2:
                    raise SyntaxError
                op2 = op_stack.pop()
                op1 = op_stack.pop()
                result = 0
                match token:
                    case '*':
                        result = op1 * op2
                    case '/':
                        result = op1 / op2
                    case '+':
                        result = op1 + op2
                    case '-':
                        result = op1 - op2
                op_stack.push(result)
            else:
                op_stack.push(int(token))

        if op_stack.size() != 1:
            raise SyntaxError
        
        return float(op_stack.pop())
    else:
        return float(token_list[0])

#################### INFIX TO POSTFIX ####################
def in2post(expr):
    if type(expr) is not str:
        raise ValueError("in2post - Expression is not a string")
    op_stack = Stack()
    output = []
    token_list = [x for x in expr]

    if len(token_list) > 0:
        for token in token_list:
            if token in ["(",")","*","/","+","-"]:
                if op_stack.size() > 0 or token == "(":
                    match token:
                        case "(":
                            op_stack.push(token)
                        case ")":
                            operator = ""
                            while operator != "(":
                                if op_stack.size() < 1:
                                    raise SyntaxError
                                operator = op_stack.pop()
                                if operator in ["*", "/", "+", "-"]:
                                    output.append(operator)
                        case "*":
                            while op_stack.size() > 0 and op_stack.top() in ['*', '/']:
                                output.append(op_stack.pop())
                            op_stack.push(token)
                        case "/":
                            while op_stack.size() > 0 and op_stack.top() in ['*', '/']:
                                output.append(op_stack.pop())
                            op_stack.push(token)
                        case "+":
                            while op_stack.size() > 0 and op_stack.top() in ['*', '/', '+', '-']:
                                output.append(op_stack.pop())
                            op_stack.push(token)
                        case "-":
                            while op_stack.size() > 0 and op_stack.top() in ['*', '/', '+', '-']:
                                output.append(op_stack.pop())
                            op_stack.push(token)
                else:
                    op_stack.push(token)
            else:
                if token == " ":
                    continue
                output.append(token)

        while op_stack.size() > 0:
            output.append(op_stack.pop())
            
        return ' '.join(output)
    else:
        return token_list[0]


#################### MAIN ####################
def main():
    # Read in the expressions from data.txt
    with open('data.txt') as file:
        expressions = file.readlines()
    
    for expression in expressions:
        # Remove newline characters
        expression = expression.strip()

        # Run functions and output results
        print(f'infix: {expression}')
        pf_expression = in2post(expression)
        print(f'postfix: {pf_expression}')
        print(f'answer: {eval_postfix(pf_expression)}\n')

    
if __name__=="__main__":
    main()