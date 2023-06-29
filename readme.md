# Interactive Equation Manipulator

This is a graphical user interface application that allows you to interactively manipulate algebraic equations.

## Usage

After starting the application, you will see an input box where you can enter an algebraic equation in the form of 'lhs = rhs' (e.g. 'x + 2 = 4'). 

### Supported Operations 

- '+n', '-n', '*n', '/n' to add, subtract, multiply, or divide both sides of the equation by 'n'.

You can also check the "Verbose" checkbox if you want a message after each interaction.

### Example Session

1. Start the application by running `python main.py`.
2. In the input box, enter an equation like `3x+2=3` and press Enter.
3. The current equation will be displayed in the output box.
4. Enter `+5` in the input box and press Enter. The equation will be updated to `3*x + 7 = 8`.
5. Enter `+3x**5` in the input box and press Enter. The equation will be updated to `3*x**5 + 3*x + 7 = 3*x**5 + 8`.
6. Enter `/3x**7` in the input box and press Enter. The equation will be updated to `(3*x**5 + 3*x + 7)/(3*x**7) = (3*x**5 + 8)/(3*x**7)`.
7. Enter `solve` in the input box and press Enter. The solution `x = [1/3]` will be displayed in the output box.
8. Enter `-3` in the input box and press Enter. The equation will be updated to `-3 + (3*x**5 + 3*x + 7)/(3*x**7) = -3 + (3*x**5 + 8)/(3*x**7)`.
9. Enter `solve` in the input box and press Enter. The solution `x = [1/3]` will be displayed in the output box.

If an error occurs while processing your equation input, an error message will be displayed in red text below the input box.