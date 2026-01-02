import json
import random
import re

# Load intents
with open(r"C:\Users\Sam\Desktop\FAQ_Chatbot\intents.json", "r") as file:
    data = json.load(file)

def get_response(user_input):
    user_input = user_input.lower()

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            if re.search(pattern, user_input):
                return random.choice(intent["responses"])

    return "Sorry, I didn't understand that. Please try asking differently."

print("🤖 College FAQ Chatbot")
print("Type 'exit' to end the chat\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Bot: Goodbye! 👋")
        break

    response = get_response(user_input)
    print("Bot:", response)
