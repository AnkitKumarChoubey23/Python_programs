# Ask for the size of the array
size = int(input("Enter the size of the array: "))

# Initialize an empty array
arr = []

# Take input for each element
print(f"Enter {size} elements:")
for i in range(size):
    val = int(input(f"Element {i + 1}: "))
    arr.append(val)

# Display the array
print("Your array:", arr)

# Ask for the element to search
target = int(input("Enter the element to find: "))

# Search for the element
if target in arr:
    position = arr.index(target)
    print(f"✅ Element found at position {position} (0-based index).")
else:
    print("❌ Element not found in the array.")