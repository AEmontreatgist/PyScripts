def function1():
    print("Function 1 called")
    
def function2():
    print("Function 2 called")
    
def function3():
    print("Function 3 called")
    
def function4():
    print("Function 4 called")
    
def function5():
    print("Function 5 called")
    
while True:
    print("Select a function to execute:")
    print("1. Function 1")
    print("2. Function 2")
    print("3. Function 3")
    print("4. Function 4")
    print("5. Function 5")
    print("0. Exit program")
    choice = int(input("Enter your choice: "))
    if choice == 0:
        print("Exiting program...")
        break
    elif choice == 1:
        function1()
    elif choice == 2:
        function2()
    elif choice == 3:
        function3()
    elif choice == 4:
        function4()
    elif choice == 5:
        function5()
    else:
        print("Invalid choice, please try again.")

