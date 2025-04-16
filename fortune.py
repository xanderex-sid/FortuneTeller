# fortune.py (v1.1)

import random

print("🔮 Welcome to Siddharth Mishra's Fortune Teller (21JE0918) 🔮")
mood = input("How are you feeling today? (happy/sad/neutral/stressed): ").lower()

fortunes = {
    "happy": [
        "✨ Your fortune: Great things await you, Siddharth! Keep smiling. ✨",
        "🌟 Your fortune: Joy surrounds you — embrace every moment!",
    ],
    "sad": [
        "💧 Your fortune: Don't worry Siddharth, Storms don't last forever. Better days are coming.",
        "🌈 Your fortune: A rainbow will follow this rain — hang in there.",
    ],
    "neutral": [
        "🌤️ Your fortune: Calm seas make skilled sailors. Stay steady.",
        "🧘 Your fortune: Stillness is power. You’re aligned, Siddharth.",
    ],
    "stressed": [
        "😌 Your fortune: Take a deep breath, Siddharth. Peace is within reach.",
        "🕊️ Your fortune: Even the busiest bees rest — don’t forget to pause.",
    ]
}

if mood in fortunes:
    print(random.choice(fortunes[mood]))
else:
    print("🤔 Hmm... I can't read that mood. Try happy, sad, neutral, or stressed.")

