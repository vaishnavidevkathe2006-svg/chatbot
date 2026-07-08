# Internship FAQ Chatbot

A simple Python command-line chatbot that answers frequently asked questions about internship opportunities. The chatbot also maintains a chat history by logging all conversations with timestamps.

## Features

- Interactive command-line chatbot
- Answers common internship-related questions
- Keyword-based response matching
- Stores chat history in a log file
- Timestamped conversation records
- Simple and beginner-friendly Python project

## Technologies Used

- Python 3
- datetime module
- File handling

## Project Structure

```
project/
│── internship_bot.py
│── chat_log.txt      (created automatically after first chat)
│── README.md
```

## Installation

1. Clone the repository or download the project.

```bash
git clone https://github.com/your-username/internship-faq-chatbot.git
```

2. Navigate to the project folder.

```bash
cd internship-faq-chatbot
```

3. Run the chatbot.

```bash
python internship_bot.py
```

## Available Questions

You can ask questions related to:

- hello
- roles
- stipend
- duration
- apply
- eligibility
- remote
- certificate

Example:

```
You: stipend
Bot: We offer ₹15,000 to ₹25,000 per month based on skills.
```

## Example Conversation

```
Bot: Welcome to TechCorp Internships! I'm your assistant. Type 'quit' to exit.

You: hello
Bot: Hi! Ask me about roles, stipend, duration, or application process.

You: roles
Bot: Open roles: Python Developer, Web Dev, Data Analyst, UI/UX Designer.

You: apply
Bot: Apply here: careers.techcorp.com/intern. Send resume to hr@techcorp.com

You: quit
Bot: All the best for your application!
```

## Chat Logging

Every conversation is automatically saved in **chat_log.txt**.

Example log:

```
[2026-07-08 10:30] You: hello
[2026-07-08 10:30] Bot: Hi! Ask me about roles, stipend, duration, or application process.

[2026-07-08 10:31] You: stipend
[2026-07-08 10:31] Bot: We offer ₹15,000 to ₹25,000 per month based on skills.
```

## How It Works

1. Displays a welcome message.
2. Accepts user input.
3. Searches for matching keywords in the FAQ dictionary.
4. Returns the appropriate response.
5. Logs both user and bot messages with timestamps.
6. Exits when the user types `quit`.

## Future Enhancements

- Add Natural Language Processing (NLP)
- GUI using Tkinter or PyQt
- Voice-enabled chatbot
- Database integration
- Web version using Flask or Django
- AI-powered responses

## Author

Developed as a Python mini project for learning file handling, dictionaries, loops, and functions.

## License

This project is free to use for educational and learning purposes.
