import speech_recognition as sr
import cohere
import pyttsx3

# Initialize Cohere API client with your API key
co = cohere.Client('BFPd9QCU7qbRLIoHbDrhAp10uxEr595ILJbVmpsC')  # Replace with your actual API key

# Function to convert audio to text
def audio_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak something:")
        audio = recognizer.listen(source)
        
    try:
        text = recognizer.recognize_google(audio)
        print("You said: ", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand the audio.")
        return ""
    except sr.RequestError:
        print("Sorry, there was an error with the audio service.")
        return ""

# Function to generate response using Cohere
def generate_response(conversation_history):
    response = co.generate(
        model='command',  # Or you can choose another model
        prompt=conversation_history,
        max_tokens=100,
        temperature=0.7  # Controls the randomness of the output
    )
    return response.generations[0].text.strip()

# Function to convert text to audio using pyttsx3 (directly in the terminal)
def text_to_audio(text):
    engine = pyttsx3.init()

    # Setting up voice properties
    voices = engine.getProperty('voices')
    # You can change the voice index here to select a different voice (depending on your OS)
    engine.setProperty('voice', voices[1].id)  # Use a more natural-sounding voice (try 0 or 1)
    
    # Adjusting speed of speech (optional for more human-like behavior)
    engine.setProperty('rate', 150)  # Speed of speech (normal is around 150-200)
    engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)

    # Speak the text
    engine.say(text)
    engine.runAndWait()

# Main Function for continuous conversation
def main():
    conversation_history = ""  # To maintain context of the conversation
    
    print("Chatbot is ready! You can start talking. Type 'exit' to end.")
    
    while True:
        # Step 1: Convert Audio to Text
        text_input = audio_to_text()
        
        if text_input.lower() == 'exit':  # Allow user to exit the conversation
            print("Exiting the conversation.")
            break
        
        # Add the new question to the conversation history
        conversation_history += f"You: {text_input}\n"
        
        # Step 2: Generate Response using Cohere
        response = generate_response(conversation_history)
        
        # Add the response to the conversation history
        conversation_history += f"Chatbot: {response}\n"
        
        # Step 3: Convert Response to Audio (plays directly in terminal)
        print("Chatbot: " + response)
        text_to_audio(response)  # This will speak the response in the terminal

if __name__ == "__main__":
    main()
