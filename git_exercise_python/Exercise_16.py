# Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
# D 100
# W 200

# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500


net_amount = 0

while True:
    transaction = input("Enter transaction (leave empty to stop): ")
    if not transaction:
        break

    type, amount = transaction.split()
    amount = int(amount)

    if type == 'D':
        net_amount += amount
    elif type == 'W':
        net_amount -= amount

print(f"The net amount is: {net_amount}")
