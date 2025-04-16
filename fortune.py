# fortune.py (v1.2)

import random

print("🔮 Welcome to Siddharth Mishra's Fortune Teller (21JE0918) 🔮")

mood = input("How are you feeling today? (happy/sad/neutral/stressed/excited): ").lower()

fortunes = {
    "happy": [
        "✨ Your fortune: Great things await you, Siddharth! Keep smiling. ✨",
        "🌟 Your fortune: Your joy will attract positivity today!",
        "🎉 Your fortune: Something wonderful is coming your way!"
    ],
    "sad": [
        "💫 Your fortune: Even the darkest night will end and the sun will rise.",
        "❤️ Your fortune: Take care, Siddharth. Better days are on their way.",
        "🌈 Your fortune: Rainbows follow the rain—stay strong!"
    ],
    "neutral": [
        "🔮 Your fortune: Siddharth, sometimes no news is good news. Stay balanced.",
        "🍀 Your fortune: Keep doing what you're doing—consistency pays off!",
        "✨ Your fortune: A small surprise will make your day brighter."
    ],
    "stressed": [
        "🧘‍♂️ Your fortune: Breathe in, breathe out. Peace is within reach.",
        "🛡️ Your fortune: You’ve handled worse—today will be easier than you expect.",
        "💆‍♂️ Your fortune: Take a break, Siddharth. You deserve it!"
    ],
    "excited": [
        "🚀 Your fortune: Siddharth, use your energy to build something amazing today!",
        "🔥 Your fortune: Let your excitement drive you to success!",
        "🌟 Your fortune: This spark will light a fire in others too—go lead!"
    ]
}

if mood in fortunes:
    print(random.choice(fortunes[mood]))
else:
    print("🤔 Mood not recognized, but your future is still full of mystery and potential!")

