import datetime

def log_chat(user, bot):
    with open("chat_log.txt", "a") as f:
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        f.write(f"[{time}] You: {user}\n[{time}] Bot: {bot}\n\n")

def internship_bot():
    print("Bot: Welcome to TechCorp Internships! I'm your assistant. Type 'quit' to exit.")
    
    faqs = {
        "hello": "Hi! Ask me about roles, stipend, duration, or application process.",
        "roles": "Open roles: Python Developer, Web Dev, Data Analyst, UI/UX Designer.",
        "stipend": "We offer ₹15,000 to ₹25,000 per month based on skills.",
        "duration": "Internship period is 3 months, with PPO chance.",
        "apply": "Apply here: careers.techcorp.com/intern. Send resume to hr@techcorp.com",
        "eligibility": "B.Tech/BCA/MCA students in final/pre-final year can apply.",
        "remote": "Yes, we have hybrid and fully remote options.",
        "certificate": "You get an internship certificate + LOR on completion."
    }

    while True:
        user_msg = input("You: ").lower().strip()
        if user_msg == 'quit':
            reply = "All the best for your application!"
            print(f"Bot: {reply}")
            log_chat(user_msg, reply)
            break

        reply = "Sorry, I didn't get that. Try asking about 'roles', 'stipend', or 'apply'."
        for key in faqs:
            if key in user_msg:
                reply = faqs[key]
                break
        
        print(f"Bot: {reply}")
        log_chat(user_msg, reply)

if __name__ == "__main__":
    internship_bot()
