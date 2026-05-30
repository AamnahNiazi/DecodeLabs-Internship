total_damage = 0

print("Welcome to the Wallet Weeper 3000!")

while True:
    wallet_pain = input(
        "Enter what you just spent (or type 'cry' to see the damage): "
    )

    if wallet_pain.lower() == "cry":
        break

    regret = float(wallet_pain)
    total_damage = total_damage + regret
    print("Ouch!!! Moving on...  ")

print("---")
print("Grand total of your poor life choices:", total_damage)
print("Time to eat instant noodles for the rest of the month! :( ")