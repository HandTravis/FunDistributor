print("how many players? ")
people = int(input())
balances = []
depleted = [False for _ in range(people)]
names = []

# Collecting names and balances
for p in range(people):
    print("What is your name: ")
    name = input()
    names.append(name)
    print(name, ", input your amount gained/owed (add minus sign for lost money): ")
    balances.append(float(input()))

# Initialize the pay_to dictionary after names are populated
pay_to = {name: [] for name in names}

# Distributing the amounts between losers and winners
for i, amount in enumerate(balances):
    if amount != 0:
        depleted[i] = False
        if amount > 0:
            for j in range(people):
                if depleted[i]:
                    break
                elif depleted[j]:
                    continue
                if balances[j] < 0:  # Loser found
                    if abs(balances[j]) < amount:
                        amount += balances[j]  # Reduce the amount by the loser's debt
                        pay_to[names[j]].append((names[i], abs(balances[j])))  # Record payment
                        balances[j] = 0  # Loser is now paid off
                        depleted[j] = True
                    else:
                        balances[j] -= amount  # Reduce the loser's debt
                        pay_to[names[j]].append((names[i], abs(amount)))  # Record full payment
                        amount = 0  # Winner has no more to distribute
                        depleted[i] = True  # Mark winner as done

# Output who owes what
for payee, payers in pay_to.items():
    if payers:
        print("player " + payee + " owes these people: ")
        for payer, amount in payers:
            print(amount, " to " + payer)
