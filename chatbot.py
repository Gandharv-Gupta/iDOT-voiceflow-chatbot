# chatbot.py
# Main conversational loop connecting speech-to-text, LLM, and text-to-speech modules

from speech_to_text import speech_to_text  # Function to get user speech as text
from call_groq import call_groq  # Function to get LLM response
from text_to_speech import text_to_speech  # Function to speak text


def main():
    print("Say 'quit' or 'exit' to stop the conversation.")
    while True:
        print("Listening...")
        user_text = speech_to_text()
        if not user_text:
            print("Didn't catch that. Please try again.")
            continue
        print(f"You said: {user_text}")
        if user_text.lower() in ["quit", "exit"]:
            print("Exiting chatbot.")
            break
        response = call_groq(user_text)
        print(f"Bot: {response}")
        text_to_speech(response)
        chat_history = []
        # Add user message to history
        chat_history.append(f"User: {user_text}")
        # Pass chat history as a string
        history_str = '\n'.join(chat_history[-6:])  # last 6 turns for brevity
        response = call_groq(user_text, chat_history=history_str)
        print(f"Bot: {response}")
        # Add bot response to history
        chat_history.append(f"Bot: {response}")


if __name__ == "__main__":
    main()
