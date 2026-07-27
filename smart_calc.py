print("=== SOHOM ER SMART CALCULATOR ===")

num1 = float(input("First number de: "))
op = input("Ki korbi? +, -, *, / : ").strip()
num2 = float(input("Second number de: "))

if op == "+":
    print("Jogfol:", num1 + num2)
elif op == "-":
    print("Biyogfol:", num1 - num2)
elif op == "*":
    print("Gunfol:", num1 * num2)
elif op == "/":
    if num2 != 0:
        print("Bhagfol:", num1 / num2)
    else:
        print("0 diye bhag kora jay na Boss!")
else:
    print("Bhuler operator dili Boss!")
