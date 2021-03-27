import speech_recognition as sr

def get_transcript():
  r = sr.Recognizer()
  file_audio = sr.AudioFile('recording/recording.wav')

  with file_audio as source:
    audio_text = r.record(source)

  transcript = r.recognize_google(audio_text)
  return transcript

trans = get_transcript()