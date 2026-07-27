#!/bin/bash
clear
figlet "SYSTEM BOOT" | toilet -f term -F gay
sleep 1
echo "Loading Music Player.exe..." | toilet -f term -F gay
sleep 1
clear

figlet "NOW PLAYING" | toilet -f term -F gay
echo "━━━━━━━━━━━━" | toilet -f term -F gay
echo "Itni Si Sazish - FULL ❤️" | toilet -f term -F gay
echo "━━━━━━━━━━━━" | toilet -f term -F gay
sleep 2

termux-media-player play /sdcard/Music/song/Itni_Si_Sazish.mp3 &

sleep 2
echo "Itni si sazis karle" | toilet -f term -F gay
sleep 2.7
echo "Duniya se harzis karle" | toilet -f term -F gay
sleep 2.7
echo "Ak dil me dharke badal" | toilet -f term -F gay
sleep 2.7
echo "Itni gundais karle" | toilet -f term -F gay
sleep 2.7
echo "Mere lahejeme teri sada hain" | toilet -f term -F gay
sleep 2.7
echo "Meri akhome tera pata hain" | toilet -f term -F gay
sleep 2.7
echo "Me tuj metu mujme chupa hain" | toilet -f term -F gay
sleep 2.7
echo "Hain ishq ja" | toilet -f term -F gay

sleep 4
termux-media-player stop

echo ""
figlet "THE END" | toilet -f term -F gay
