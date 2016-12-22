# Create a program that prints whether a name 
# is long

name = "Shefali"

# See if the length of the name counts as long
if len(name) > 8:
    # If the name is long, say so
    print("That's a long name")
# If the name is moderate 
elif len(name) < 8: 
    print("That's a moderate name")
# If the name is short
else len(name) < 5:
    print("That's a short name")