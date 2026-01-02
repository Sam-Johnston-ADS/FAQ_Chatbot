# 🤖 FAQ Chatbot (Rule-Based NLP Project)

## 📌 Project Overview
This project is a **Rule-Based FAQ Chatbot** developed using Python and basic NLP techniques.  
The chatbot answers frequently asked questions by matching user input with predefined patterns and responses.

This project is suitable for **beginners in Natural Language Processing (NLP)** and demonstrates how simple chatbots work without using machine learning models.

---

## 🎯 Features
- Responds to common FAQ queries
- Keyword and pattern matching using regular expressions
- Easy to customize and extend
- Lightweight and fast
- No training or dataset required

---

## 🛠 Technologies Used
- Python 3
- JSON (for storing intents and responses)
- Regular Expressions (regex)

---

## 📁 Project Structure
FAQ_Chatbot/
├── chatbot.py # Main chatbot program
├── intents.json # Questions (patterns) and responses
├── README.md # Project documentation
└── requirements.txt # Project dependencies
---
### 💬 Sample Conversation
You: hi
Bot: Hello! How can I help you?

You: hostel
Bot: Yes, hostel facilities are available for both boys and girls.

You: bye
Bot: Goodbye! Have a great day 😊
---
### 🧠 How It Works

- User enters a question

- Input is converted to lowercase

- The chatbot checks for matching keywords using regex

- A suitable response is returned from the intents file

- If no match is found, a default response is shown
---
### 🎓 Learning Outcomes

Understanding rule-based chatbots

Basics of Natural Language Processing

Pattern matching using regex

Working with JSON data in Python

---

### 🙋 Author

Sam Johnston C
B.Tech – Artificial Intelligence & Data Science
