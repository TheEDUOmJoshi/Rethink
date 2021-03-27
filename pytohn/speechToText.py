import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()
# use mic.list_microphone_names() to see device index


r.dynamic_energy_threshold = False

def from_mic(recognizer, microphone):
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("recognizer must be Recognizer instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("microphone must be Microphone instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, phrase_time_limit=15)

    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return "unrecognized"
    except sr.RequestError:
        return "unrecognized"

while True:
    print(from_mic(r, mic))