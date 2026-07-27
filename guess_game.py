import random

print("=== SOHOM ER GUESS GAME ===")
secret = random.randint(1, 50)
print("Ami 1 theke 50 er moddhe ekta number vebechhi")

while True:
    guess = int(input("Tor guess de: "))
    
    if guess == secret:
        print("MILE GACHE BOSS! Tui Legend 🔥🏆")
        break
    elif guess < secret:
        print("Aro boro number de")
    else:
        print("Aro chhoto number de")
