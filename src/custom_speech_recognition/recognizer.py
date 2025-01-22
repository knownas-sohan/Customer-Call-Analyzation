import speech_recognition as sr

def speech_to_text(duration=60):
    """Capture audio from the microphone and convert it to text using Google Web Speech API."""
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Welcome to WiFi Customer Quick Help Agent! Describe your problem in 60 seconds.")
            recognizer.adjust_for_ambient_noise(source, duration=0.9)
            print("Listening for 1 minute... Please speak.")
            
            # Record audio for a fixed duration
            audio = recognizer.record(source, duration=duration)
            return recognizer.recognize_google(audio)
    except sr.RequestError as e:
        print(f"API request error: {e}")
        return None
    except sr.UnknownValueError:
        print("Unable to understand the audio.")
        return None
