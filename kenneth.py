def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_operation():
    operations = ['+', '-', '*', '/']
    while True:
        op = input("Enter operation (+, -, *, /): ")
        if op in operations:
            return op
        else:
            print("Invalid operation. Please enter one of +, -, *, /.")

def perform_calculation(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2

def calculator():
    while True:
        print("Simple Calculator")
        
        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")
        operation = get_operation()
        
        result = perform_calculation(num1, num2, operation)
        print(f"The result of {num1} {operation} {num2} is: {result}")
        
        cont = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if cont != 'yes':
            print("Exiting the calculator. Goodbye!")
            break

# Start the calculator program
if __name__ == "__main__":
    calculator()
