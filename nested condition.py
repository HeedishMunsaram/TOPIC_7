num1 = float(input("Pick a number: "))
num2 = float(input("Pick another number: "))

if num1 <= num2 :
    if num1 == num2 :
        print("Equal")
    else:
        print("Not equal!")
elif num1 > num2 :
    print("Greater!")
else:
    print("Less!")