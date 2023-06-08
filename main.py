import re
from sympy import symbols, Eq, solve, parse_expr

usage = """
### INTERACTIVE EQUATION MANIPULATOR ###
USAGE:
- Enter an equation in the form of 'lhs = rhs' (e.g. 'x + 2 = 4')
- You can use the following operators: +, -, *, /
- You can use the following features: simplify, expand, solve
- Symbolic manipulation is allowed

Note:
- To quit the application, simply type 'quit'.

### Enjoy manipulating your equations!
"""


verbose = False

def preprocess_equation(eq):
    processed_eq = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', eq)
    processed_eq = re.sub(r'(\d)(\()', r'\1*\2', processed_eq)
    processed_eq = re.sub(r'(\))([a-zA-Z\d])', r'\1*\2', processed_eq)
    return processed_eq


def parse_input(user_input, lhs, rhs):
    if user_input == 'simplify':
        lhs = lhs.simplify()
        rhs = rhs.simplify()
        message = "Simplified equation"
    elif user_input == 'expand':
        lhs = lhs.expand()
        rhs = rhs.expand()
        message = "Expanded equation"
    elif user_input == 'solve':
        solution = solve(Eq(lhs, rhs))
        message = f"x = {solution}"
    elif user_input.startswith("+"):
        to_add = parse_expr(preprocess_equation(user_input[1:]))
        lhs += to_add
        rhs += to_add
        message = f"Added {to_add} to both sides of the equation"
    elif user_input.startswith("-"):
        to_subtract = parse_expr(preprocess_equation(user_input[1:]))
        lhs -= to_subtract
        rhs -= to_subtract
        message = f"Subtracted {to_subtract} from both sides of the equation"
    elif user_input.startswith("*"):
        to_multiply = parse_expr(preprocess_equation(user_input[1:]))
        lhs *= to_multiply
        rhs *= to_multiply
        message = f"Multiplied both sides of the equation by {to_multiply}"
    elif user_input.startswith("/"):
        to_divide = parse_expr(preprocess_equation(user_input[1:]))
        lhs /= to_divide
        rhs /= to_divide
        message = f"Divided both sides of the equation by {to_divide}"
    else:
        message = "Invalid input"
    return lhs, rhs, message


def main():
    print(usage)
    x = symbols('x')
    user_equation = input('What equation would you like to work with? ')
    user_equation = preprocess_equation(user_equation)
    lhs_str, rhs_str = user_equation.split("=")
    lhs = parse_expr(lhs_str, locals())
    rhs = parse_expr(rhs_str, locals())
    print(f"Current equation: {lhs} = {rhs}")

    while True:
        print(f"\n{lhs} = {rhs}")
        user_input = input(" ")
        if user_input == 'quit':
            break
        else:
            lhs, rhs, message = parse_input(user_input, lhs, rhs)
            if verbose:
                print(message)


if __name__ == "__main__":
    main()