
## Usage

After starting the script, enter an algebraic equation in the form of 'lhs = rhs' (e.g. 'x + 2 = 4'). 

### Supported Operations 
- '+n', '-n', '*n', '/n' to add, subtract, multiply, or divide both sides of the equation by 'n'.
- 'simplify' to simplify both sides of the equation.
- 'expand' to expand both sides of the equation.
- 'solve' to solve the equation for 'x'.

Type 'quit' to exit the script.

Here is an example session:

```bash
❯ python main.py

### INTERACTIVE EQUATION MANIPULATOR ###
USAGE:
- Enter an equation in the form of 'lhs = rhs' (e.g. 'x + 2 = 4')
- You can use the following operators: +, -, *, /
- You can use the following features: simplify, expand, solve
- Symbolic manipulation is allowed

Note:
- To quit the application, simply type 'quit'.

### Enjoy manipulating your equations!

What equation would you like to work with? 3x+2=3
Current equation: 3*x + 2 = 3
3*x + 2 = 3
 +5
Added 5 to both sides of the equation
3*x + 7 = 8
 +3x**5
Added 3*x**5 to both sides of the equation
3*x**5 + 3*x + 7 = 3*x**5 + 8
 /3x**7
Divided both sides of the equation by 3*x**7
(3*x**5 + 3*x + 7)/(3*x**7) = (3*x**5 + 8)/(3*x**7)
 solve
x = [1/3]
(3*x**5 + 3*x + 7)/(3*x**7) = (3*x**5 + 8)/(3*x**7)
 -3
Subtracted 3 from both sides of the equation
-3 + (3*x**5 + 3*x + 7)/(3*x**7) = -3 + (3*x**5 + 8)/(3*x**7)
 solve
x = [1/3]
```
