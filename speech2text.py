import speech_recognition as sr

filename = "NLP-Assignment-Recording.wav"
r = sr.Recognizer()

with sr.AudioFile(filename) as source:
    audio_data = sr.Recognizer().record(source)

    text = sr.Recognizer().recognize_google(audio_data)
    print(text)

