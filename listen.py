import speech_recognition as sr


#initialize recognizer
recognizer = sr.Recognizer()
recognizer.pause_threshold = 0.5

def Listen():
    # use default microphone as the source
    with sr.Microphone() as source:
        print("Speak anything ...")
    
        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source)
        
        # Listen to the user's input
        audio_data = recognizer.listen(source)
    
        try:
            print("Recognizing...")
        
            # Recognize speech using Google Speech Rcognition
            text = recognizer.recognize_google(audio_data)
            print(f"Speech recognized: {text}")
            return text
        except sr.UnknownValueError:
            print("Could not undrstand the audio.")
            return None
        except sr.RequestError as e:
            print(f"Error: {e}")
            return None

Listen()