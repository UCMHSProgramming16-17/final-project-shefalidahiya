count = 0
while count < 5:
    num = int(input("please give me a number"))
    if (num % 2) == 0:
        print("This is an even number")
    else:
        print("This is an odd number")
    count += 1
if count >= 5:
    print("This loop is complete")