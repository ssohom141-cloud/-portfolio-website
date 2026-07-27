#!/bin/bash
clear
figlet "SYSTEM BOOT" | toilet -f term -F gay
sleep 2
echo "Loading Love.exe..." | toilet -f term -F gay
sleep 2
clear

figlet "RISHITA" | toilet -f term -F gay
sleep 2
clear

echo "━━━━━━━━━━━━" | toilet -f term -F gay
echo "🚨 I LOVE YOU RISHITA 🚨" | toilet -f term -F gay
echo "━━━━━━━━━━━━" | toilet -f term -F gay
sleep 2

echo ""
echo "Playing: Itni Si Sazish ❤️" | toilet -f term -F gay

# SONG START - FULL BAJBE
termux-media-player play /sdcard/Music/song/Itni_Si_Sazish.mp3 &

# LYRICS TIMING ER SATHE
sleep 6
echo "Itni si sazish kar le..." | toilet -f term -F gay
sleep 8
echo "Duniya saari kar le..." | toilet -f term -F gay
sleep 8
echo "Ik dil mein dhadke baadal..." | toilet -f term -F gay
sleep 8
echo "Itni gunda ishq kar le..." | toilet -f term -F gay
sleep 10
echo "RISHITA... main tujhmein tu mujhmein chupa hai" | toilet -f term -F gay

# SONG ER TIME ER JONNO WAIT KOR - 2 MIN 50 SEC
sleep 170

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
