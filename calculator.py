def calculator():
    while True:
        try:
            num1=float(input("Enter the first number.\n"))
        except ValueError:
            print("It is not number, try again")
            continue

        while True:
            try:
                num2=float(input("Enter the second number\n"))
            except ValueError:
                print("It is not number, try again")
                continue   
            operator=input("+,-,*,/")
            if operator == "+":
                num1=num1+num2
                print(num1)
            elif operator =="-":
                num1=num1-num2
                print(num1)
            elif operator =="*":
                num1=num1*num2
                print(num1)
            elif operator =="/":
                try:
                    num1=num1/num2
                    print(num1)
                except ZeroDivisionError:
                    print("You can not divide by zero!")
                    continue
            else:
                print("You can only use the following operators: +, -, /,*.")

                                
            new_task=input("Do you want to continue? yes/no\n")
            if new_task != "yes":
                break

calculator()
                                        
                                    
                                    
    
    



