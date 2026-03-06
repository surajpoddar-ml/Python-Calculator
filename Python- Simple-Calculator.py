def main():
    while True:
        print("Simple Calculator for Second Project")
        print("A. Addition")
        print("S. Subtraction")
        print("M. Multiplication")
        print("D. Division")
        print("E. Exit")
        
        user_choice = input("Select an operation (A/S/M/D/E): ").upper()
    
        
        if user_choice == 'E':
            print("Exiting the calculator. Goodbye!")
            break
        
        if user_choice in ['A', 'S', 'M', 'D']:
            try:
                first_number = float(input("Enter first number: "))
                second_number = float(input("Enter second number: "))
            except ValueError:
                print("Error: Please enter valid numeric values.")
                continue
            
            if user_choice == 'A':
                calculation_result = first_number + second_number
                print(f"Result: {first_number} + {second_number} = {calculation_result}")
            
            elif user_choice == 'S':
                calculation_result = first_number - second_number
                print(f"Result: {first_number} - {second_number} = {calculation_result}")
            
            elif user_choice == 'M':
                calculation_result = first_number * second_number
                print(f"Result: {first_number} × {second_number} = {calculation_result}")
            
            elif user_choice == 'D':
                if second_number == 0:
                    print("Error: Division by zero is not allowed.")
                else:
                    calculation_result = first_number / second_number
                    print(f"Result: {first_number} ÷ {second_number} = {calculation_result}")
        else:
            print("Please choose A, S, M, D, or E.")

main()
