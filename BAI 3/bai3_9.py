# This function adds two numbers  
def add(x, y): 
    return x + y 

# This function subtracts two numbers  
def subtract(x, y): 
    return x - y 

# This function multiplies two numbers 
def multiply(x, y): 
    return x * y 

# This function divides two numbers 
def divide(x, y): 
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Take input from the user  
choice = input("Enter choice (1/2/3/4): ") 

# Kiểm tra đầu vào hợp lệ cho số
try:
    num1 = float(input("Enter first number: ")) 
    num2 = float(input("Enter second number: "))
except ValueError:
    print("Invalid input! Please enter a numeric value.")
    exit()

# Thực hiện phép toán dựa trên lựa chọn
if choice == '1': 
    print(num1, "+", num2, "=", add(num1, num2)) 
elif choice == '2': 
    print(num1, "-", num2, "=", subtract(num1, num2)) 
elif choice == '3': 
    print(num1, "*", num2, "=", multiply(num1, num2)) 
elif choice == '4': 
    result = divide(num1, num2)
    print(num1, "/", num2, "=", result) 
else: 
    print("Invalid input")
print ("sinh vien: TRan Van Tien Dat")
print ("Mssv: 235752020710004")