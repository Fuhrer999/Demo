print("Simple calculator using Python.")
print("OPTIONS:")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division.")

choice = float(input("Enter your choice,1-4: "))

if choice == 1:
    a = float(input("Enter A: "))
    b = float(input("Enter B: "))
    c = a + b
    print("Sum = ",c)
elif choice == 2:
    a = float(input("Enter A: "))
    b = float(input("Enter B: "))
    c = a - b
    print("Difference = ",c)
elif choice == 3:
    a = float(input("Enter A: "))
    b = float(input("Enter B: "))
    c = a * b
    print("Product = ",c)
elif choice == 4:
    a = float(input("Enter A: "))
    b = float(input("Enter B: "))
    c = a / b
    print("Quotient = ",c)
else: 
    print("Invalid Input.")