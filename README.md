# Chatbot
# Chatbot with Speech Recognition and Cohere API
This project implements a chatbot that interacts with the user through voice. It listens to the user's voice input, processes the input using Cohere API for generating responses, and speaks the responses back to the user using pyttsx3 for text-to-speech synthesis. The conversation history is maintained so that the chatbot can answer questions in context.



# feature
1- Speech Recognition: Converts the user's spoken input into text using Google's Speech Recognition API.

2- Cohere API: Generates responses based on the input text using Cohere’s language model.

3- Text-to-Speech: Converts the chatbot’s responses back to speech using pyttsx3.

4- Continuous Conversation: The chatbot maintains the context of the conversation.

5- Voice Customization: Adjust the voice settings (rate, volume, and voice selection).



# Requirements

Before running this project, make sure you have the following:

1-Python 3.x

2-Cohere API Key: You need an API key from Cohere.

3-SpeechRecognition: For converting audio to text.

4-pyttsx3: For text-to-speech conversion.

5-pyaudio: For capturing audio from the microphone.



# Install Required Libraries
Run the following commands to install the required dependencies:

pip install SpeechRecognition pyttsx3 cohere pyaudio



# Setup

1-Get Your Cohere API Key:

   -Sign up on Cohere and get your API key.
   -Replace 'your-cohere-api-key' in the code with your actual API key.

2-Configure Voice Settings (Optional):

   -You can customize the voice properties such as speech rate, volume, and voice selection by editing the pyttsx3 settings in the text_to_audio function.
   -To view available voices on your system, you can refer to the pyttsx3 section in the script, which lists all available voices and their attributes.



# Usage
1-Running the Chatbot:

Simply run the script in terminal using Python:

python chatbot.py

  
   -The chatbot will prompt you to speak something. It will listen to your voice, convert it to text, generate a response using Cohere, and then speak the response back to you.

2-Exit the Conversation:

   -To exit the conversation, say exit, and the chatbot will stop.



# Troubleshooting

1-Speech Recognition Issues:

   -Ensure your microphone is working and properly connected.

   -If the bot cannot recognize speech, try speaking clearly or adjusting the microphone sensitivity.

2-Audio Playback:

   -If there is an issue with the audio playback (especially on Windows), ensure the correct audio device is selected as the default output device.

3-API Key Errors:

   -Ensure your Cohere API key is valid and correctly pasted in the script.



# Contributions:

If you'd like to contribute to this project, feel free to fork the repository, open issues, or submit pull requests. Your input is always welcome!

Thank you for exploring this chatbot, and happy coding! 🚀
   
