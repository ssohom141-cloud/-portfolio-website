#!/bin/bash
clear
figlet "SYSTEM BOOT" | toilet -f term -F gay
sleep 1
echo "Loading Love.exe..." | toilet -f term -F gay
sleep 1
clear

figlet "RISHITA" | toilet -f term -F gay
sleep 1
clear

echo "━━━━━━━━━━━━" | toilet -f term -F gay
echo "🚨 I LOVE YOU RISHITA 🚨" | toilet -f term -F gay
echo "━━━━━━━━━━━━" | toilet -f term -F gay
sleep 1

echo ""
echo "Playing: Itni Si Sazish ❤️" | toilet -f term -F gay

# SONG START
termux-media-player play /sdcard/Music/song/Itni_Si_Sazish.mp3 &

# LYRICS FAST - 3 SEC GAP
sleep 3
echo "Itni si sazish kar le..." | toilet -f term -F gay
sleep 3
echo "Duniya saari kar le..." | toilet -f term -F gay
sleep 3
echo "Ik dil mein dhadke baadal..." | toilet -f term -F gay
sleep 3
echo "Itni gunda ishq kar le..." | toilet -f term -F gay
sleep 3
echo "Main tujhmein tu mujhmein chupa hai" | toilet -f term -F gay
sleep 3
echo "RISHITA sun le zara..." | toilet -f term -F gay
sleep 3
echo "I LOVE YOU RISHITA ❤️" | toilet -f term -F gay

# BAKI SONG ER JONNO WAIT
sleep 140

# SONG STOP
termux-media-player stop

echo ""
echo "Dil.exe status: CRASHED FOR YOU" | toilet -f term -F gay
sleep 1

read -p "Do you accept? [Y/N]: " ans
if [ "$ans" = "Y" ] || [ "$ans" = "y" ]; then
    figlet "ACCEPTED" | toilet -f term -F gay
    echo "✅ Forever With RISHITA v99.0 LOADED ❤️👑"
else
    figlet "TRY AGAIN" | toilet -f term -F gay
    echo "❌ Will ask till YES"
fi
