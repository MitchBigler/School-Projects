from stack import Stack

#################### EVALUATE POSTFIX ####################
def eval_postfix(expr):
    if type(expr) is not str:
        raise ValueError("Expression is not a string")
    op_stack = Stack()
    token_list = [x for x in expr]
    print(token_list)

    if len(token_list) > 0:
        for token in token_list:
            if token == " ":
                continue
            elif token in ["*","/","+","-"]:
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
        return float(op_stack.pop())
    else:
        return float(token_list[0])

#################### INFIX TO POSTFIX ####################
def in2post(expr):
    op_stack = Stack()

    return "NA"


#################### MAIN ####################
def main():
    # Read in the expressions from data.txt
    with open('data.txt') as file:
        expressions = file.readlines()

    print('\n')
    print(expressions)
    print('\n')
    
    for expression in expressions:
        # Remove newline characters
        expression = expression.strip()

        # Run functions and output results
        print(f'infix: {expression}')
        pf_expression = in2post(expression)
        print(f'postfix: {pf_expression}')
        #print(f'answer: {eval_postfix(pf_expression)}\n')

    print(eval_postfix("71-"))

    
if __name__=="__main__":
    main()