# create list
sequence = []

while True:
    # ask user to define input
    choice = input("feed me ")
    # if user inputs "stop"
    if choice == "stop":
    # break function
        break
    # otherwise add user input to list
    sequence.append(choice)
# print sequence
print(sequence)
    
