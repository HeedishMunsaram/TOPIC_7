name =""

while True:
    name = input("Enter a one-word name, friends use to greet you: ")
    if name.isalpha():
        print("\nNice to meet you", name.title())
        break
    else:
        print("\nSorry, enter one-word using letters only")