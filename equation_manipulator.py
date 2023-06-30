import tkinter as tk
from tkinter import ttk, messagebox
from equation_parser import preprocess_equation, parse_input
from sympy import symbols, parse_expr
from constants import verbose, usage, equation_input_error, operational_input_error

class EquationManipulator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Interactive Equation Manipulator")

        self.verbose = tk.BooleanVar()
        self.verbose.set(verbose)

        self.create_widgets()
        self.create_menu()

        self.grid_columnconfigure(0, weight=1)
        for i in range(6):
            self.grid_rowconfigure(i, weight=1)

        self.update_idletasks()

        self.minsize(self.winfo_width(), self.winfo_height())


    def create_widgets(self):
        self.output_label = ttk.Label(self, text="Output:")
        self.output_label.grid(column=0, row=0, padx=5, pady=5, sticky='w')

        self.output_text = tk.Text(self)
        self.output_text.grid(column=0, row=1, padx=5, pady=5, sticky='nsew')

        self.input_label = ttk.Label(self, text="Enter your equation or action:")
        self.input_label.grid(column=0, row=2, padx=5, pady=5, sticky='w')

        self.input_entry = ttk.Entry(self)
        self.input_entry.grid(column=0, row=3, padx=5, pady=5, sticky='ew')
        self.input_entry.bind('<Return>', lambda event: self.submit_input())

        self.verbose_checkbutton = ttk.Checkbutton(self, text="Verbose", variable=self.verbose)
        self.verbose_checkbutton.grid(column=0, row=4, padx=5, pady=5, sticky='w')

        self.error_label = ttk.Label(self, text="", foreground="red")
        self.error_label.grid(column=0, row=5, padx=5, pady=5, sticky='w')

    def create_menu(self):
        self.menubar = tk.Menu(self)
        self.helpmenu = tk.Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="Usage", command=self.show_usage)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)
        self.config(menu=self.menubar)

    def show_usage(self):
        messagebox.showinfo("Usage", usage)

    def submit_input(self):
        user_input = self.input_entry.get()
        self.input_entry.delete(0, tk.END)
        try:
            if "=" in user_input:
                user_input = preprocess_equation(user_input)
                lhs_str, rhs_str = user_input.split("=")
                if not self.is_valid_expression(lhs_str) or not self.is_valid_expression(rhs_str):
                    raise ValueError(equation_input_error)
                x = symbols('x')
                self.lhs = parse_expr(lhs_str, locals())
                self.rhs = parse_expr(rhs_str, locals())
                self.output_text.insert(tk.END, f"Current equation: {self.lhs} = {self.rhs}\n")
            else:
                if not hasattr(self, 'lhs') or not hasattr(self, 'rhs'):
                    raise ValueError(equation_input_error)
                self.lhs, self.rhs, message = parse_input(user_input, self.lhs, self.rhs)
                if self.verbose.get():
                    self.output_text.insert(tk.END, f"{message}\n")
                self.output_text.insert(tk.END, f"{self.lhs} = {self.rhs}\n")
        except ValueError as e:
            self.error_label['text'] = str(e)
        except Exception as e:
            self.error_label['text'] = operational_input_error
        self.input_entry.focus_set()

    def is_valid_expression(self, expr):
        # Check if the expression is valid
        try:
            parse_expr(expr)
            return True
        except Exception:
            return False