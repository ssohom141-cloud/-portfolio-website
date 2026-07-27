#!/bin/bash
clear
figlet "SYSTEM BOOT" | toilet -f term -F gay
sleep 1
echo "Loading modules..." | toilet -f term -F gay
sleep 1
echo "[███████░░░] 70%" | toilet -f term -F gay
sleep 0.5
echo "[██████████] 100%" | toilet -f term -F gay
sleep 1
clear
echo "⚠️  TARGET LOCKED  ⚠️" | toilet -f term -F gay
sleep 1
figlet "RISHITA" | toilet -f term -F gay
sleep 1
echo "Heart Rate: 160 bpm 💓" | toilet -f term -F gay
echo "Status: Dil.exe CRASHED x2" | toilet -f term -F gay
sleep 2
clear
echo "━━━━━━━━━━" | toilet -f term -F gay
echo "     🚨 CRITICAL ALERT 🚨     " | toilet -f term -F gay
echo "━━━━━━━━━━" | toilet -f term -F gay
echo "Error: I LOVE YOU RISHITA ❤️" | toilet -f term -F gay  
echo "Debug: Life = NULL without you" | toilet -f term -F gay
echo "Solution: Marry Me Proposal" | toilet -f term -F gay
echo "━━━━━━━━━━" | toilet -f term -F gay
sleep 2
echo ""
read -p "Do you accept? [Y/N]: " ans
if [ "$ans" = "Y" ] || [ "$ans" = "y" ]; then
    figlet "ACCEPTED" | toilet -f term -F gay
    echo "✅ Connection: STABLE ❤️👑"
    echo "Loading Forever With RISHITA v99.0..."
else
    figlet "ERROR 404" | toilet -f term -F gay
    echo "❌ Reason Not Found"
    echo "Will Try Again Till You Say YES..."
fi
