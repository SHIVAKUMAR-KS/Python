def add(x,y):
            return x+y
def substract(x,y):
        return x-y
def multiply(x,y):
        return x*y
def divide(x,y):
        if y!=0:
                return x/y
        else:
                return "cannot be divide"


def calculator():
        print("Simple calculator::")
        print("1: Add:")
        print("2: Substract:")
        print("3: multiply:")
        print("4: divide:")

        choice=input("Enter the choice:1/2/3/4 ::")

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                        print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                        print(f"{num1} - {num2} = {substract(num1, num2)}")
            elif choice == '3':
                        print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                        result = divide(num1, num2)
                        print(f"{num1} / {num2} = {result}")
            else:
                        print("Invalid input. Please enter a valid choice.")
        else:
            print("Invalid input. Please enter a valid choice.")

calculator()

        
