import sympy as sp

# Define the variable
x = sp.Symbol('x')

# Get equation from user
equation = input("Enter an equation (e.g., 1/4*x + 3 = 7): ")

try:
    # Split equation into left and right side
    left, right = equation.split("=")
    
    # Convert both sides into symbolic expressions
    left_expr = sp.sympify(left)
    right_expr = sp.sympify(right)
    
    # Solve the equation
    solution = sp.solve(left_expr - right_expr, x)
    
    # Display the solution(s)
    if solution:
        print("Solution(s):", solution)
    else:
        print("No real solution found.")
except Exception as e:
    print("Invalid equation! Please enter a valid format.")
