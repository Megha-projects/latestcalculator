def add(x,y):
    return x + y
def sub(x,y):
    return x - y
def mul(x,y):
    return x * y
def div(x,y):
    return x / y
def pow(x,y):
    return x ** y
#take input from user
print("select Oeration")
print("1.Add")
print("2.Subtraction")
print("3.Multiple")
print("4.Divide")
print("5.Power")
choice = input("Enter Choice(1/2/3/4/5):")
a = int(input("Enter First Num :"))
b = int(input("Enter Second Num :"))

if choice == '1':
    print(a, "+", b,"=",add(a,b))
elif choice == '2':
    print(a, "-", b,"=",sub(a,b))
elif choice == '3':
    print(a, "*", b,"=",mul(a,b))
elif choice == '4':
    print(a, "/", b,"=",div(a,b))
elif choice == '5':
    print(a, "**", b,"=",pow(a,b))
else:
    print("invalid input")
   