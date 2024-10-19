from stack import Stack

def eval_postfix(expr):
    return "NA"

def in2post(expr):
    return "NA"

def main():
    # Read in the expressions from data.txt
    with open('data.txt') as file:
        expressions = file.readlines()

    print(expressions)
    for expression in expressions:
        # Remove newline characters
        expression = expression.strip()

        # Run functions and output results
        print(f'infix: {expression}')
        print(f'postfix: {in2post(expression)}')
        print(f'answer: {eval_postfix(expression)}\n')

    
if __name__=="__main__":
    main()