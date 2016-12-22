cats = {"Fred": "black and white", "Maurice": "black and white", "Aaron Purr": "grey tabby"}

print(cats["Fred"])

quantities= {"bubble tea": 5, "chocolate cake": 3, "asparagus": 5, "tears of exhausted teenagers": 60}

print(quantities["tears of exhausted teenagers"])

print(list(quantities.keys())[0])

del(quantities["asparagus"])
print(quantities.keys())

quantities["fake glasses"] = 1
print(quantities.keys())

for key, value in cats.items():
    print(key, 'is', value)