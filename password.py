password = input("Password de Boss: ")

length = len(password)
boro_hat = False
chhoto_hat = False
number = False

for ch in password:
    if ch.isupper():
        boro_hat = True
    elif ch.islower():
        chhoto_hat = True
    elif ch.isdigit():
        number = True

print("\n=== PASSWORD REPORT ===")
print(f"Length: {length}")

if length >= 8 and boro_hat and chhoto_hat and number:
    print("Strong Password Boss! 🔥 Hacker o dhukte parbe na")
else:
    print("Weak Password 😅 Aro strong banate hobe")
    if length < 8:
        print("- 8 ta character de")
    if not boro_hat:
        print("- Boro hater letter de (A-Z)")
    if not chhoto_hat:
        print("- Chhoto hater letter de (a-z)")
    if not number:
        print("- Number de (0-9)")
