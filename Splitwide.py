def splitwise():
    # Step 1: Input the number of people and their names
    num_people = int(input("Enter the number of people involved: "))
    names = []
    for i in range(num_people):
        name = input(f"Enter name of person {i+1}: ")
        names.append(name)

    # Step 2: Input the total amount spent by each person
    expenses = {}
    total_spent = 0
    for name in names:
        amount = float(input(f"Enter amount spent by {name}: "))
        expenses[name] = amount
        total_spent += amount

    # Calculate average spending per person
    average_spent = total_spent / num_people

    # Step 3: Calculate the balance for each person
    balance = {}
    for name in names:
        balance[name] = expenses[name] - average_spent

    # Step 4: Determine who owes money and to whom
    print("\nBalances:")
    for name, bal in balance.items():
        if bal > 0:
            print(f"{name} should take {bal:.2f}")
        elif bal < 0:
            print(f"{name} should give {-bal:.2f}")
        else:
            print(f"{name} is settled.")

    # Simplify debts (optional, for optimization)
    print("\nDebt Summary:")
    givers = {name: -bal for name, bal in balance.items() if bal < 0}
    takers = {name: bal for name, bal in balance.items() if bal > 0}

    for giver, giver_amt in givers.items():
        for taker, taker_amt in list(takers.items()):
            if giver_amt == 0:
                break
            settlement = min(giver_amt, taker_amt)
            print(f"{giver} gives {settlement:.2f} to {taker}")
            givers[giver] -= settlement
            takers[taker] -= settlement
            if takers[taker] == 0:
                del takers[taker]

# Run the program
splitwise()