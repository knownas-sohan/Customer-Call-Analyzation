import pyttsx3

def text_to_speech(text):
    """Convert the generated text into spoken audio."""
    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Text-to-speech error: {e}")
