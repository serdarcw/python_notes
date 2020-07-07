  
while True:
    n = input("Please enter your number : ")
    if not n.isdigit():
        print("your entry is not valid entry, please use positive number")
    else:
        if sum([int(i)**len(n) for i in n]) == int(n):
            print(f"{n} is an Armstrong number")
        else:
            print(f"{n} isn't an Armstrong number")