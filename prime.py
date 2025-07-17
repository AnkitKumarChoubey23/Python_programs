# Ask the user to enter a number
num = int(input("Enter a number to check if it's prime: "))

# Prime check logic
if num <= 1:
    print("❌ Not a prime number.")
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("❌ Not a prime number.")
            break
    else:
        print("✅ It's a prime number!")
print("\u274C")