print("=== SOHOM ER PRO TO-DO LIST ===")

while True:
    print("\n1. Kaj Add kor")
    print("2. List dekha") 
    print("3. Kaj Delete kor")
    print("4. Ber ho")
    
    choice = input("Ki korbi? 1/2/3/4: ")
    
    if choice == "1":
        kaj = input("Notun kaj lekh: ")
        file = open("tasks.txt", "a")
        file.write(kaj + "\n")
        file.close()
        print("Kaj file e save hoye gelo Boss ✅")
    
    elif choice == "2":
        print("\n=== TOR SAVED KAJER LIST ===")
        try:
            file = open("tasks.txt", "r")
            tasks = file.readlines()
            file.close()
            if len(tasks) == 0:
                print("Kono kaj nai Boss 😎")
            else:
                for i in range(len(tasks)):
                    print(f"{i+1}. {tasks[i].strip()}")
        except:
            print("Kono kaj nai Boss 😎")
    
    elif choice == "3":
        try:
            file = open("tasks.txt", "r")
            tasks = file.readlines()
            file.close()
            
            if len(tasks) == 0:
                print("Delete korar moto kaj nei 😅")
            else:
                print("\nKon number kaj delete korbi?")
                for i in range(len(tasks)):
                    print(f"{i+1}. {tasks[i].strip()}")
                
                num = int(input("Number de: "))
                tasks.pop(num-1)
                
                file = open("tasks.txt", "w")
                for t in tasks:
                    file.write(t)
                file.close()
                print("Kaj delete hoye gelo Boss 🗑️")
        except:
            print("Kichu ekta vul holo Boss 😅")
    
    elif choice == "4":
        print("Bye Boss! File e sob save ache 🔥")
        break
    
    else:
        print("1, 2, 3, 4 er moddhe de Boss!")
