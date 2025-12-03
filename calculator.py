
def numbers():
    result=0
    while True:
        try:
            first_number=float(input("Enter the first number\n"))
            second_number=float(input("Enter the second number\n"))
            operator=input("Choose the operation you want (+, -,*, /)\n")
            if operator=="+":
                result=first_number+second_number
                print(f"Result is {result}")
            elif operator=="-":
                result=first_number-second_number
                print(f"Result is {result}")
            elif operator =="/":
                try:
                    result=first_number/second_number
                    print(f"Result is {result}")
                except ZeroDivisionError:
                    print("It is not possible to devine by zero")
                
            elif operator=="*":
                result=first_number*second_number
                print(f"Result is {result}")
            else:
                print("You can only use the following operators: +, -, /,*.")
                

            break
        except ValueError:
            print("The entered value is not a number!")

     

    
    
numbers()


