# TYPEWRITER FUNCTION
typewriter() {
    text="$1"
    for (( i=0; i<${#text}; i++ )); do
        echo -n "${text:$i:1}"
        sleep 0.05
    done
    echo ""
}

clear
typewriter "=================================="
typewriter " WELCOME BOSS SOHOM"
typewriter "=================================="
typewriter "[1] Hacking Mode"
typewriter "[2] Coding Mode"
typewriter "[3] Exit"
typewriter "=================================="
read -p "Select an option: " choice

# IP BER KORAR FUNCTION
get_ip() {
    curl -s ifconfig.me
}

# BATTERY % BER KORAR FUNCTION
get_battery() {
    termux-battery-status | grep percentage | cut -d":" -f2 | cut -d"," -f1
}

if [ $choice -eq 1 ]; then
    clear
    typewriter "HACKING MODE ACTIVATED..."
    sleep 0.5
    toilet -f big "SOHOM"
    figlet -f slant "Hacker Online"
    echo ""
    typewriter "📍 Diamond Harbor | $(date +"%d-%m-%Y %H:%M")"
    typewriter "🌐 IP: $(get_ip)"
    typewriter "🔋 Battery: $(get_battery)%"

elif [ $choice -eq 2 ]; then
    clear
    typewriter "CODING MODE ACTIVATED..."
    sleep 0.5
    toilet -f big "SOHOM"
    figlet -f slant "Coder Online"
    echo ""
    typewriter "📍 Diamond Harbor | $(date +"%d-%m-%Y %H:%M")"
    typewriter "🌐 IP: $(get_ip)"
    typewriter "🔋 Battery: $(get_battery)%"

elif [ $choice -eq 3 ]; then
    clear
    typewriter "Goodbye Boss 👑"
    exit
else
    typewriter "Wrong option boss!"
fi
