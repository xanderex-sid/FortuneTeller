# fortune.py (v1.0)

print("🔮 Welcome to Siddharth Mishra's Fortune Teller (21JE0918) 🔮")
mood = input("How are you feeling today? (happy/sad/neutral): ").lower()

if mood == "happy":
    print("✨ Your fortune: Great things await you, Siddharth! Keep smiling. ✨")
elif mood == "sad":
    print("💧 Your fortune: Siddharth, Storms don't last forever. Better days are coming.")
elif mood == "neutral":
    print("🌤️ Your fortune: Calm seas make skilled sailors. Stay steady.")
else:
    print("🤔 Hmm... I can't read that mood. Try happy, sad, or neutral.")

