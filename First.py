# Program to enter numbers into a file

# File name
file_name = "numbers.txt"

try:
    with open(file_name, "w") as file:
        print("Enter numbers one by one. Type 'done' to finish.")
        
        while True:
            user_input = input("Enter a number (or 'done' to finish): ")
            
            if user_input.lower() == "done":
                break
            
            try:
                # Check if the input is a number
                number = float(user_input)
                file.write(f"{number}\n")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    
    print(f"Numbers have been successfully written to {file_name}")
except IOError:
    print("An error occurred while accessing the file.")

# Program to read float numbers from a file and store them in an array (list)

# File name
file_name = "numbers.txt"

# Initialize an empty list to store the floats
float_array = []

try:
    with open(file_name, "r") as file:
        for line in file:
            try:
                # Convert each line to a float and append it to the list
                number = float(line.strip())
                float_array.append(number)
            except ValueError:
                # Handle lines that do not contain valid float numbers
                print(f"Invalid entry in file: {line.strip()} (skipped)")
    
    print("Numbers successfully read into the array:", float_array)
except FileNotFoundError:
    print(f"File '{file_name}' not found. Please ensure the file exists.")
except IOError:
    print("An error occurred while accessing the file.")


# Sorting the array in ascending order
float_array.sort()

print("Sorted array in ascending order:", float_array)

try:
    with open(file_name, "a") as file:  # 'a' mode is used to append to the file
        file.write("The number sorted in Ascending order is : ")
        for number in float_array:
            file.write(f"{number}\n")
    
    print(f"Numbers have been successfully appended to {file_name}")
except IOError:
    print("An error occurred while accessing the file.")

# To sort in descending order, you can use:
float_array.sort(reverse=True)
print("Sorted array in descending order:", float_array)
try:
    with open(file_name, "a") as file:  # 'a' mode is used to append to the file
        file.write("The number sorted in Descending order is : ")
        for number in float_array:
            file.write(f"{number}\n")
    
    print(f"Numbers have been successfully appended to {file_name}")
except IOError:
    print("An error occurred while accessing the file.")


