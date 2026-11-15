print("==================================================================\n                       PYTHON CALCULATOR\n==================================================================")
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Click '+' for addition\n" "Click '-' for subtraction\n" "Click '*' for multiplication\n" "Click '/' for division\n")
    o = input("Enter operation to perform: ")

    match o:
        case "+":
            print(f"The answer is {a+b}.")
        case "-":
            print(f"The answer is {a-b}.")
        case "*":
            print(f"The answer is {a*b}.")
        case "/":
            print(f"The answer is {a/b}.")
        case default:
            print("Invalid Option")
except ValueError :
    print("Invalid values for numbers!")