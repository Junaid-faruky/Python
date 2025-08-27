responses = {
    "hello": "Hi there!",
    "how are you": "I’m good, thanks!",
    "bye": "Goodbye!"
}

while True:
    msg = input("You: ").lower()
    if msg in responses:
        print("Bot:", responses[msg])
    else:
        print("Bot: Sorry, I don’t understand.")
    if msg == "bye":
        break
