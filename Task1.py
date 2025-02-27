import re

def chatbot():
    print("Chatbot: Hi! I am your rule-based chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if re.search(r'bye|goodbye', user_input, re.IGNORECASE):
            print("Chatbot: Goodbye! Have a great day!")
            break
        elif re.search(r'hi|hello|hey', user_input, re.IGNORECASE):
            print("Chatbot: Hello! How can I assist you today?")
        elif re.search(r'how are you', user_input, re.IGNORECASE):
            print("Chatbot: I am just a bot, but I am doing great! How about you?")
        elif re.search(r'what is your name', user_input, re.IGNORECASE):
            print("Chatbot: I am a chatbot created to assist you with your questions.")
        elif re.search(r'(.*) your (favorite|favourite) (.*)', user_input, re.IGNORECASE):
            print("Chatbot: I do not have preferences, but I enjoy helping you!")
        elif re.search(r'thank you|thanks', user_input, re.IGNORECASE):
            print("Chatbot: You are welcome! If you have more questions, feel free to ask.")
        else:
            print("Chatbot: I'm sorry, I don't understand that. Can you please rephrase?")

chatbot()
