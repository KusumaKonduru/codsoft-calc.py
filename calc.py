# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Main function to run the calculator
def main():
    print("Welcome to Simple Calculator!")
    print("Operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    
    print("4. Division")

    # Take user input for operation choice
    choice = input("Enter operation number (1/2/3/4): ")

    # Check if the choice is valid
    if choice in ('1', '2', '3', '4'):
        # Prompt the user to enter two numbers

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            result = add(num1, num2)
            print(f"{num1} + {num2} = {result}")
        elif choice == '2':
            result = subtract(num1, num2)
            print(f"{num1} - {num2} = {result}")
        elif choice == '3':
            result = multiply(num1, num2)
            print(f"{num1} * {num2} = {result}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"{num1} / {num2} = {result}")
    else:
        print("Invalid input. Please enter a valid operation number (1/2/3/4).")

# Entry point of the program
if __name__ == "__main__":
    main()
