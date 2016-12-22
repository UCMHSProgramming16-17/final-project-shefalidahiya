fruits = ["grapes", "oranges", "apples", "grapes", "bananas", "raspberries", "grapes" ]

fruits.append("pears")
fruits.append("blueberries")


# put watermelon before oranges
fruits.insert(1, "watermelon")
fruits.insert(5, "honeydew")
fruits.remove("apples")

fruits.remove("raspberries")
fruits.insert(6, "peaches")
fruits.remove("peaches")
fruits.insert(5, "peaches")

print(fruits)
print(fruits.pop(2)) # pop oranges out of the list and print it
print(fruits)
print(fruits.pop()) # pop blueberries out
print("honeydew is at index", fruits.index("honeydew"))
print(fruits.count("grapes"))
fruits.sort()
print(fruits)