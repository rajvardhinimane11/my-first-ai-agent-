print("🤖 Simple AI Chatbot")
print("Type 'bye' to exit.\n")

def chatbot(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you?"

    elif "how are you" in user_input:
        return "I'm doing great! Thanks for asking."

    elif "your name" in user_input:
        return "I am a simple AI chatbot."

    elif "python" in user_input:
        return "Python is a popular programming language used for AI and data science."

    elif "ai" in user_input or "artificial intelligence" in user_input:
        return "AI means Artificial Intelligence. It enables computers to perform intelligent tasks."

    elif "thank" in user_input:
        return "You're welcome! 😊"

    elif "bye" in user_input:
        return "Goodbye! Have a nice day!"

    else:
        return "Sorry, I don't understand that yet."

while True:
    user = input("You: ")

    response = chatbot(user)
    print("Bot:", response)

    if "bye" in user.lower():
        break