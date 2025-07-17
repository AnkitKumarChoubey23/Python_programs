'''
# Ask the user for their name
name = input("Enter your name: ")

# Ask how many times they want the name to be printed
count = int(input("How many times should your name be printed? "))

# Print the name 'count' times
for i in range(count):
    print(f"{i + 1}: {name}")


count = int(input("How many lines for the triangle? "))

for i in range(1, count + 1):
    print("*" * i)
'''

count = int(input("How many lines for the triangle? "))

for i in range(1, count + 1):
    print( )  # Move to the next line
    for j in range(i):
        print("*")
    


#print("*", end="")