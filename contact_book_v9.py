# Contact Book V9.0 - LEGEND MODE
# Quick Link + Group Filter + Bday Countdown | Jorepatki BOSS Edition

import shutil
import csv
from datetime import datetime, timedelta

# COLOR MODES
DARK_MODE = True
def set_colors():
    global RED, GREEN, YELLOW, BLUE, PURPLE, CYAN, END
    if DARK_MODE:
        RED = '\033[91m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        BLUE = '\033[94m'
        PURPLE = '\033[95m'
        CYAN = '\033[96m'
        END = '\033[0m'
    else:
        RED = '\033[31m'
        GREEN = '\033[32m'
        YELLOW = '\033[33m'
        BLUE = '\033[34m'
        PURPLE = '\033[35m'
        CYAN = '\033[36m'
        END = '\033[0m'
set_colors()

CONTACTS_FILE = "contacts_v9.txt"

# PASSWORD LOCK
PASSWORD = "4321"
for attempt in range(3):
    user_pass = input(f"{YELLOW}Password de BOSS: {END}")
    if user_pass == PASSWORD:
        print(f"{GREEN}Access Granted! Welcome LEGEND BOSS{END}")
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
                if len(parts) == 7:
                    name, numbers, group, bday, fav, wa, photo = parts
                    contacts.append({
                        "name": name,
                        "numbers": numbers.split(","),
                        "group": group,
                        "bday": bday,
                        "fav": fav,
                        "wa": wa,
                        "photo": photo
                    })
            return contacts
    except:
        return []

def save_contacts(contacts):
    contacts.sort(key=lambda x: (x["fav"]!= "1", x["name"].lower()))
    with open(CONTACTS_FILE, "w") as file:
        for c in contacts:
            numbers_str = ",".join(c["numbers"])
            file.write(f"{c['name']}|{numbers_str}|{c['group']}|{c['bday']}|{c['fav']}|{c['wa']}|{c['photo']}\n")

def bday_countdown(bday_str):
    if bday_str == "00-00": return "N/A"
    try:
        day, month = map(int, bday_str.split("-"))
        today = datetime.now()
        year = today.year
        bday = datetime(year, month, day)
        if bday < today:
            bday = datetime(year + 1, month, day)
        delta = (bday - today).days
        if delta == 0: return "Aj!"
        elif delta == 1: return "Kal!"
        else: return f"{delta} din"
    except:
        return "N/A"

def check_birthday():
    today = datetime.now()
    today_str = today.strftime("%d-%m")
    tomorrow_str = (today + timedelta(days=1)).strftime("%d-%m")
    contacts = load_contacts()
    bday_today = []
    bday_tomorrow = []
    for c in contacts:
        if c["bday"] == today_str and c["bday"]!= "00-00":
            bday_today.append(c["name"])
        if c["bday"] == tomorrow_str and c["bday"]!= "00-00":
            bday_tomorrow.append(c["name"])

    if bday_today:
        print(f"{GREEN}Aj Birthday BOSS!{END}")
        for name in bday_today:
            print(f"{YELLOW} -> {name}{END}")
    if bday_tomorrow:
        print(f"{CYAN}Kal Birthday BOSS! Gift ready kor{END}")
        for name in bday_tomorrow:
            print(f"{YELLOW} -> {name}{END}")
    if bday_today or bday_tomorrow:
        print()

def add_contact():
    name = input(f"{CYAN}Naam lekh BOSS: {END}")
    contacts = load_contacts()
    for c in contacts:
        if c["name"].lower() == name.lower():
            print(f"{RED}BOSS {name} to already ache! Duplicate hobena{END}")
            return
    numbers = input(f"{CYAN}Number de [koma diye multi]: {END}")
    numbers_list = [n.strip() for n in numbers.split(",") if n.strip()]
    group = input(f"{CYAN}Group [Family/Friends/Office/Work]: {END}")
    if not group: group = "General"
    bday = input(f"{CYAN}Birthday [DD-MM]: {END}")
    if not bday: bday = "00-00"
    fav = input(f"{CYAN}Favourite? [1=Yes, 0=No]: {END}")
    if fav!= "1": fav = "0"
    wa = input(f"{CYAN}WhatsApp ache? [1=Yes, 0=No]: {END}")
    if wa!= "1": wa = "0"
    photo = input(f"{CYAN}Photo path [/sdcard/pic.jpg, Enter=skip]: {END}")
    if not photo: photo = "none"

    contacts.append({
        "name": name,
        "numbers": numbers_list,
        "group": group,
        "bday": bday,
        "fav": fav,
        "wa": wa,
        "photo": photo
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
            photo_icon = "P" if c["photo"]!= "none" else " "
            numbers_str = ", ".join(c["numbers"])
            bday_left = bday_countdown(c["bday"])
            print(f"{BLUE}{i}.{END} {star}{wa_icon}{photo_icon} {GREEN}{c['name']}{END} | {YELLOW}{numbers_str}{END} | {CYAN}{c['group']}{END} | Bday:{c['bday']} | Baki: {bday_left}")

def group_filter():
    group_name = input(f"{CYAN}Kon group dekhbi? [Friends/Family/Office/Work/General]: {END}")
    contacts = load_contacts()
    found = False
    print(f"\n{PURPLE}--- {group_name} Group ---{END}")
    for i, c in enumerate(contacts, 1):
        if c["group"].lower() == group_name.lower():
            star = "*" if c["fav"] == "1" else " "
            wa_icon = "WA" if c["wa"] == "1" else " "
            photo_icon = "P" if c["photo"]!= "none" else " "
            numbers_str = ", ".join(c["numbers"])
            bday_left = bday_countdown(c["bday"])
            print(f"{BLUE}{i}.{END} {star}{wa_icon}{photo_icon} {GREEN}{c['name']}{END} | {YELLOW}{numbers_str}{END} | Bday:{c['bday']} | Baki: {bday_left}")
            found = True
    if not found:
        print(f"{RED}BOSS, ei group e keu nai{END}")

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
            photo_icon = "P" if c["photo"]!= "none" else " "
            bday_left = bday_countdown(c["bday"])
            print(f"{star}{wa_icon}{photo_icon} {GREEN}{c['name']}{END} | {YELLOW}{numbers_str}{END} | {CYAN}{c['group']}{END} | Bday:{c['bday']} | Baki: {bday_left}")
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
            print(f"{YELLOW}Puran: {numbers_str} | Group: {c['group']} | Bday: {c['bday']} | Fav: {c['fav']} | WA: {c['wa']} | Photo: {c['photo']}{END}")
            new_numbers = input(f"{CYAN}Notun numbers koma diye [Enter = skip]: {END}")
            new_group = input(f"{CYAN}Notun group [Enter = skip]: {END}")
            new_bday = input(f"{CYAN}Notun birthday DD-MM [Enter = skip]: {END}")
            new_fav = input(f"{CYAN}Favourite? [1/0, Enter = skip]: {END}")
            new_wa = input(f"{CYAN}WhatsApp? [1/0, Enter = skip]: {END}")
            new_photo = input(f"{CYAN}Photo path [Enter = skip]: {END}")

            if new_numbers: c["numbers"] = [n.strip() for n in new_numbers.split(",") if n.strip()]
            if new_group: c["group"] = new_group
            if new_bday: c["bday"] = new_bday
            if new_fav in ["0","1"]: c["fav"] = new_fav
            if new_wa in ["0","1"]: c["wa"] = new_wa
            if new_photo: c["photo"] = new_photo
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
        backup_name = f"backup_v9_{time_now}.txt"
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
    csv_name = f"contacts_v9_{time_now}.csv"
    with open(csv_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Numbers", "Group", "Birthday", "Favourite", "WhatsApp", "Photo"])
        for c in contacts:
            numbers_str = ",".join(c["numbers"])
            writer.writerow([c["name"], numbers_str, c["group"], c["bday"], c["fav"], c["wa"], c["photo"]])
    print(f"{GREEN}CSV Export done BOSS! File: {csv_name}{END}")

def link_generator():
    name = input(f"{CYAN}Kar link chas BOSS? Naam lekh: {END}")
    contacts = load_contacts()
    for c in contacts:
        if c["name"].lower() == name.lower():
            if not c["numbers"]:
                print(f"{RED}BOSS, {name} er number nai{END}")
                return
            print(f"\n{PURPLE}--- {c['name']} er Numbers ---{END}")
            for i, num in enumerate(c["numbers"], 1):
                print(f"{CYAN}{i}.{END} {YELLOW}{num}{END}")

            choice = input(f"{CYAN}Kon number? [1-{len(c['numbers'])}]: {END}")
            link_type = input(f"{CYAN}Link type? [1=WhatsApp, 2=SMS]: {END}")

            try:
                idx = int(choice) - 1
                number = c["numbers"][idx].replace(" ", "").replace("+", "")
                if not number.startswith("91") and len(number) == 10:
                    number = "91" + number

                if link_type == "1" and c["wa"] == "1":
                    print(f"{GREEN}WhatsApp Link: https://wa.me/{number}{END}")
                elif link_type == "2":
                    print(f"{GREEN}SMS Link: sms:{number}{END}")
                else:
                    print(f"{RED}BOSS, WhatsApp nai or bhul choice{END}")
            except:
                print(f"{RED}Bhul choice BOSS{END}")
            return
    print(f"{RED}BOSS, ei naam e keu nai{END}")

def quick_link():
    number = input(f"{CYAN}Number de BOSS [10 digit]: {END}")
    number = number.replace(" ", "").replace("+", "")
    if not number.startswith("91") and len(number) == 10:
        number = "91" + number
    if len(number) < 10:
        print(f"{RED}BOSS bhul number{END}")
        return
    link_type = input(f"{CYAN}Link type? [1=WhatsApp, 2=SMS]: {END}")
    if link_type == "1":
        print(f"{GREEN}WhatsApp Link: https://wa.me/{number}{END}")
    elif link_type == "2":
        print(f"{GREEN}SMS Link: sms:{number}{END}")
    else:
        print(f"{RED}BOSS bhul choice{END}")

def export_to_vcf():
    contacts = load_contacts()
    if not contacts:
        print(f"{RED}BOSS, contact nai{END}")
        return
    time_now = datetime.now().strftime("%Y%m%d_%H%M%S")
    vcf_name = f"contacts_v9_{time_now}.vcf"
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
            if c['photo']!= "none":
                file.write(f"PHOTO;VALUE=URI:{c['photo']}\n")
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

def toggle_dark_mode():
    global DARK_MODE
    DARK_MODE = not DARK_MODE
    set_colors()
    mode = "DARK" if DARK_MODE else "LIGHT"
    print(f"{GREEN}BOSS {mode} MODE ON!{END}")

# BIRTHDAY CHECK ON STARTUP
check_birthday()

# Main Menu - V9.0 LEGEND MODE
while True:
    print(f"\n{PURPLE}=== CONTACT BOOK V9.0 LEGEND MODE ==={END}")
    print(f"{CYAN}1.{END} Add Contact")
    print(f"{CYAN}2.{END} View All Contact")
    print(f"{CYAN}3.{END} Search")
    print(f"{CYAN}4.{END} Edit Contact")
    print(f"{CYAN}5.{END} Delete Contact")
    print(f"{CYAN}6.{END} Backup")
    print(f"{CYAN}7.{END} Export CSV")
    print(f"{CYAN}8.{END} WA/SMS Link")
    print(f"{CYAN}9.{END} Export VCF")
    print(f"{CYAN}10.{END} Toggle Favourite")
    print(f"{CYAN}11.{END} Exit")
    print(f"{CYAN}12.{END} Dark/Light Mode")
    print(f"{CYAN}13.{END} Quick Link")
    print(f"{CYAN}14.{END} Group Filter")
    choice = input(f"{YELLOW}Tor choice [1-14]: {END}")
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
        link_generator()
    elif choice == "9":
        export_to_vcf()
    elif choice == "10":
        toggle_favourite()
    elif choice == "11":
        print(f"{GREEN}Bye BOSS. Level 19 Clear{END}")
        break
    elif choice == "12":
        toggle_dark_mode()
    elif choice == "13":
        quick_link()
    elif choice == "14":
        group_filter()
    else:
        print(f"{RED}Bhuler button BOSS. 1-14 mar{END}")
