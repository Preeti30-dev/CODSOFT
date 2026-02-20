import datetime

def chatbot():
    current_time = datetime.datetime.now().hour

    if current_time < 12:
        print("🤖 Chatbot: Good Morning!")
    elif current_time < 18:
        print("🤖 Chatbot: Good Afternoon!")
    else:
        print("🤖 Chatbot: Good Evening!")

    print("🤖 Chatbot: I am your AI chatbot.")
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower()

        if "hello" in user_input:
            print("🤖 Chatbot: Hi there! How can I help you?")
        
        elif "how are you" in user_input:
            print("🤖 Chatbot: I'm just code, but I'm doing great!")
        
        elif "your name" in user_input:
            print("🤖 Chatbot: I am CodSoft AI Chatbot.")
        
        elif "bye" in user_input:
            print("🤖 Chatbot: Goodbye! Have a great day.")
            break
        
        else:
            print("🤖 Chatbot: Sorry, I didn't understand that.")

chatbot()

