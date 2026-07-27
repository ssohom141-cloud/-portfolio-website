import time
import datetime

print("="*30)
print("  AUTO REPLY BOT ON")
print("  Bot by: Sohom")
print("="*30)
print("Note: Eta shudhu test. WhatsApp khola rakhte hobe\n")

reply_message = "Ami ekhon busy achi re ❤️ Rat e kotha bolchi - Sohom"

while True:
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"[{current_time}] Bot check korche...")
    
    # Ekhane asol e message read kora jabe na phone e
    # Tai eta demo. 10 sec por por reply pathabe
    time.sleep(10)
    print(f"Auto Reply: {reply_message}")
    print("-"*30)
    
    # Ctrl + C chaple bondho hobe
