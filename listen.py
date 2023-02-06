import speech_recognition as sr



def record_input():

    r = sr.Recognizer()

    r.energy_threshold = 19115
    r.dynamic_energy_threshold = True

    #mic = sr.Microphone(device_index=1)

    with sr.Microphone() as source:
        audio = r.record(source, duration=5)
        print("Recognizing...")

        text = r.recognize_google(audio)
        
        print(text)
        return text
        
