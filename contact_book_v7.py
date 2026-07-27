# Contact Book V7.0 - Level 17 TERMINATOR MODE
# Favourite + Multi Number + WhatsApp + VCF | Jorepatki BOSS Edition

import shutil
import csv
from datetime import datetime

# COLOR CODES
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
PURPLE = '\033[95m'
CYAN = '\033[96m'
END = '\033[0m'

CONTACTS_FILE = "contacts_v7.txt"

# PASSWORD LOCK
PASSWORD = "4321"
for attempt in range(3):
    user_pass = input(f"{YELLOW}Password de BOSS: {END}")
    if user_pass == PASSWORD:
        print(f"{GREEN}Access Granted! Welcome BOSS{END}")
        break
    else:
        print(f"{RED}Bhul password! Baki ache {2-attempt} bar{END}")
else:
    print(f"{RED}3 bar bhul! App bondho korlam. Bye BOSS{END}")
    exit()

def load_contacts():
    try:
        with open(CONTACTS_FILE, "r") as file:
            contacts = []
            for line in file:
                parts = line.strip().split("|")
                if len(parts) == 6:
                    name, numbers, group, bday, fav, wa = parts
                    contacts.append({
                        "name": name,
                        "numbers": numbers.split(","),
                        "group": group,
                        "bday": bday,
                        "fav": fav,
                        "wa": wa
                    })
            return contacts
    except:
        return []

def save_contacts(contacts):
    contacts.sort(key=lambda x: (x["fav"]!= "1", x["name"].lower()))
    with open(CONTACTS_FILE, "w") as file:
        for c in contacts:
            numbers_str = ",".join(c["numbers"])
            file.write(f"{c['name']}|{numbers_str}|{c['group']}|{c['bday']}|{c['fav']}|{c['wa']}\n")

def check_birthday():
    today = datetime.now().strftime("%d-%m")
    contacts = load_contacts()
    bday_list = []
    for c in contacts:
        if c["bday"] == today and c["bday"]!= "00-00":
            bday_list.append(c["name"])
    if bday_list:
        print(f"{GREEN}Aj Birthday BOSS!{END}")
        for name in bday_list:
            print(f"{YELLOW} -> {name}{END}")
        print()

def add_contact():
    name = input(f"{CYAN}Naam lekh BOSS: {END}")
    contacts = load_contacts()
    for c in contacts:
        if c["name"].lower() == name.lower():
            print(f"{RED}BOSS {name} to already ache! Duplicate hobena{END}")
            return
    numbers = input(f"{CYAN}Number de [koma diye multi: 7557002043,9876543210]: {END}")
    numbers_list = [n.strip() for n in numbers.split(",") if n.strip()]
    group = input(f"{CYAN}Group [Family/Friends/Office/Work]: {END}")
    if not group: group = "General"
    bday = input(f"{CYAN}Birthday [DD-MM]: {END}")
    if not bday: bday = "00-00"
    fav = input(f"{CYAN}Favourite? [1=Yes, 0=No]: {END}")
    if fav!= "1": fav = "0"
    wa = input(f"{CYAN}WhatsApp ache? [1=Yes, 0=No]: {END}")
    if wa!= "1": wa = "0"

    contacts.append({
        "name": name,
        "numbers": numbers_list,
        "group": group,
        "bday": bday,
        "fav": fav,
        "wa": wa
    })
    save_contacts(contacts)
    print(f"{GREEN}{name} save hoye gelo!{END}")

def view_contacts():
    print(f"\n{PURPLE}--- Sob Contact ---{END}")
    contacts = load_contacts()
    if not contacts:
        print(f"{RED}Kono contact nai BOSS{END}")
    else:
        for i, c in enumerate(contacts, 1):
            star = "*" if c["fav"] == "1" else " "
            wa_icon = "WA" if c["wa"] == "1" else " "
            numbers_str = ", ".join(c["numbers"])
            print(f"{BLUE}{i}.{END} {star}{wa_icon} {GREEN}{c['name']}{END} | {YELLOW}{numbers_str}{END} | {CYAN}{c['group']}{END} | Bday:{c['bday']}")

def search_contact():
    query = input(f"{CYAN}Naam/Number/Group diye khuj BOSS: {END}")
    contacts = load_contacts()
    found = False
    print(f"\n{PURPLE}--- Search Result ---{END}")
    for c in contacts:
        numbers_str = ",".join(c["numbers"])
        if (query.lower() in c["name"].lower() or
            query in numbers_str or
            query.lower() in c["group"].lower()):
            star = "*" if c["fav"] == "1" else " "
            wa_icon = "WA" if c["wa"] == "1" else " "
            print(f"{star}{wa_icon} {GREEN}{c['name']}{END} | {YELLOW}{numbers_str}{END} | {CYAN}{c['group']}{END} | Bday:{c['bday']}")
            found = True
    if not found:
        print(f"{RED}BOSS, kichu paini{END}")

def edit_contact():
    edit_name = input(f"{CYAN}Kar data edit korbi BOSS? Naam lekh: {END}")
    contacts = load_contacts()
    found = False
    for c in contacts:
        if c["name"].lower() == edit_name.lower():
            numbers_str = ",".join(c["numbers"])
            print(f"{YELLOW}Puran: {numbers_str} | Group: {c['group']} | Bday: {c['bday']} | Fav: {c['fav']} | WA: {c['wa']}{END}")
            new_numbers = input(f"{CYAN}Notun numbers koma diye [Enter = skip]: {END}")
            new_group = input(f"{CYAN}Notun group [Enter = skip]: {END}")
            new_bday = input(f"{CYAN}Notun birthday DD-MM [Enter = skip]: {END}")
            new_fav = input(f"{CYAN}Favourite? [1/0, Enter = skip]: {END}")
            new_wa = input(f"{CYAN}WhatsApp? [1/0, Enter = skip]: {END}")

            if new_numbers: c["numbers"] = [n.strip() for n in new_numbers.split(",") if n.strip()]
            if new_group: c["group"] = new_group
            if new_bday: c["bday"] = new_bday
            if new_fav in ["0","1"]: c["fav"] = new_fav
            if new_wa in ["0","1"]: c["wa"] = new_wa
            found = True
            break
    if found:
        save_contacts(contacts)
        print(f"{GREEN}{edit_name} update hoye gelo BOSS!{END}")
    else:
        print(f"{RED}BOSS, ei naam e keu nai{END}")

def delete_contact():
    delete_name = input(f"{CYAN}Kake uriye dibi BOSS? Naam lekh: {END}")
    contacts = load_contacts()
    new_contacts = [c for c in contacts if c["name"].lower()!= delete_name.lower()]
    if len(new_contacts)!= len(contacts):
        save_contacts(new_contacts)
        print(f"{RED}{delete_name} ke ure dilam BOSS!{END}")
    else:
        print(f"{RED}BOSS, ei naam e keu chilo na{END}")

def backup_contacts():
    try:
        time_now = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f"backup_v7_{time_now}.txt"
        shutil.copy(CONTACTS_FILE, backup_name)
        print(f"{GREEN}Backup done BOSS! File: {backup_name}{END}")
    except:
        print(f"{RED}BOSS, backup fail{END}")

def export_to_csv():
    contacts = load_contacts()
    if not contacts:
        print(f"{RED}BOSS, contact nai{END}")
        return
    time_now = datetime.now().strftime("%Y%m%d_%H%M%S")
    csv_name = f"contacts_v7_{time_now}.csv"
    with open(csv_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Numbers", "Group", "Birthday", "Favourite", "WhatsApp"])
        for c in contacts:
            numbers_str = ",".join(c["numbers"])
            writer.writerow([c["name"], numbers_str, c["group"], c["bday"], c["fav"], c["wa"]])
    print(f"{GREEN}CSV Export done BOSS! File: {csv_name}{END}")

def whatsapp_link():
    name = input(f"{CYAN}Kar WhatsApp link chas BOSS? Naam lekh: {END}")
    contacts = load_contacts()
    for c in contacts:
        if c["name"].lower() == name.lower():
            if c["wa"] == "1" and c["numbers"]:
                main_number = c["numbers"][0].replace(" ", "").replace("+", "")
                if not main_number.startswith("91") and len(main_number) == 10:
                    main_number = "91" + main_number
                print(f"{GREEN}WhatsApp Link: https://wa.me/{main_number}{END}")
                print(f"{YELLOW}Browser e paste kore chat kor BOSS{END}")
            else:
                print(f"{RED}BOSS, {name} er WhatsApp nai{END}")
            return
    print(f"{RED}BOSS, ei naam e keu nai{END}")

def export_to_vcf():
    contacts = load_contacts()
    if not contacts:
        print(f"{RED}BOSS, contact nai{END}")
        return
    time_now = datetime.now().strftime("%Y%m%d_%H%M%S")
    vcf_name = f"contacts_v7_{time_now}.vcf"
    with open(vcf_name, "w") as file:
        for c in contacts:
            file.write("BEGIN:VCARD\n")
            file.write("VERSION:3.0\n")
            file.write(f"N:{c['name']};;;;\n")
            file.write(f"FN:{c['name']}\n")
            for num in c["numbers"]:
                file.write(f"TEL;TYPE=CELL:{num}\n")
            file.write(f"CATEGORIES:{c['group']}\n")
            if c['bday']!= "00-00":
                day, month = c['bday'].split("-")
                file.write(f"BDAY:2024-{month}-{day}\n")
            file.write("END:VCARD\n")
    print(f"{GREEN}VCF Export done BOSS! File: {vcf_name}{END}")
    print(f"{YELLOW}Phone er Contact app e Import kor{END}")

def toggle_favourite():
    name = input(f"{CYAN}Kake Favourite korbi/hatabi BOSS? Naam lekh: {END}")
    contacts = load_contacts()
    for c in contacts:
        if c["name"].lower() == name.lower():
            c["fav"] = "0" if c["fav"] == "1" else "1"
            save_contacts(contacts)
            status = "Favourite" if c["fav"] == "1" else "Unfavourite"
            print(f"{GREEN}{name} ke {status} kore dilam BOSS!{END}")
            return
    print(f"{RED}BOSS, ei naam e keu nai{END}")

# BIRTHDAY CHECK ON STARTUP
check_birthday()

# Main Menu - Level 17 TERMINATOR MODE
while True:
    print(f"\n{PURPLE}=== CONTACT BOOK V7.0 TERMINATOR MODE ==={END}")
    print(f"{CYAN}1.{END} Add Contact")
    print(f"{CYAN}2.{END} View All Contact")
    print(f"{CYAN}3.{END} Search")
    print(f"{CYAN}4.{END} Edit Contact")
    print(f"{CYAN}5.{END} Delete Contact")
    print(f"{CYAN}6.{END} Backup")
    print(f"{CYAN}7.{END} Export CSV")
    print(f"{CYAN}8.{END} WhatsApp Link")
    print(f"{CYAN}9.{END} Export VCF")
    print(f"{CYAN}10.{END} Toggle Favourite")
    print(f"{RED}11.{END} Exit")
    choice = input(f"{YELLOW}Tor choice [1-11]: {END}")
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        edit_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        backup_contacts()
    elif choice == "7":
        export_to_csv()
    elif choice == "8":
        whatsapp_link()
    elif choice == "9":
        export_to_vcf()
    elif choice == "10":
        toggle_favourite()
    elif choice == "11":
        print(f"{GREEN}Bye BOSS. Level 17 Clear{END}")
        break
    else:
        print(f"{RED}Bhuler button BOSS. 1-11 mar{END}")
