import speech_recognition
# from Demos.getfilever import lang

robot_ear = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
    print("Robot: I'am listening!!!")
    audio  = robot_ear.listen(mic)

# you = robot_ear.recognize_google(audio,language='en')
try:
    you = robot_ear.recognize_google(audio)
except:
    you = ""
print("You"+you)

# pip install SpeechRecognition
# pip install pyaudio