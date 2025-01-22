from utils.env_loader import load_environment
from custom_speech_recognition.recognizer import speech_to_text
from watsonx.model import initialize_model, generate_response
from watsonx.prompts import generate_prompt
from text_to_speech.tts import text_to_speech

def main():
    # Step 1: Load environment variables
    load_environment()
    
    print("Starting the WiFi troubleshooting assistant...")
    
    # Step 2: Convert speech to text
    speech_text = speech_to_text()
    if speech_text:
        print("You said:", speech_text)
    else:
        print("No valid speech input detected.")
        return
    
    # Step 3: Initialize the AI model
    model = initialize_model()
    
    # Step 4: Generate a prompt and get a response
    prompt = generate_prompt(speech_text)
    response = generate_response(model, prompt)
    print("AI Response:\n", response)
    
    # Step 5: Convert the response to speech
    text_to_speech(response)

if __name__ == "__main__":
    main()
