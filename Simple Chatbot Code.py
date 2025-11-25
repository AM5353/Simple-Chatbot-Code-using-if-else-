# Simple Rule-Based Chatbot using if-else

print("Chatbot: Hello! I am your simple chatbot. Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "hi" or user == "hello":
        print("Chatbot: Hello! How can I help you?")
    elif "name" in user:
        print("Chatbot: I am a simple rule-based chatbot!")
    elif "help" in user:
        print("Chatbot: Sure! I can answer basic questions.")
    elif "bye" in user:
        print("Chatbot: Goodbye! Have a great day.")
        break
    else:
        print("Chatbot: Sorry, I didn’t understand that.")

