# create a starting length
sequence = [1,1]
# specify desired length
s_length = 15

while len(sequence) < s_length:
    # TO DO: get new value by adding last two items
    new_val = sequence[-1] + sequence[-2]
    # add a value to the end of list
    sequence.append(new_val)

count = 1
# print each each item in list
for number in sequence:
    print(str(count) + ".", number)
# increase count for each run
    count +=1

