import speech_recognition
import pyttsx3
from datetime import date, datetime


# listen
robot_ear = speech_recognition.Recognizer()
robot_mouth= pyttsx3.init()
robot_brain = ""
while True:
    with speech_recognition.Microphone() as mic:
        print("Robot: I'am listening!!!")
        audio  = robot_ear.listen(mic)
    print("Robot: ...")

    # you = robot_ear.recognize_google(audio,language='en')
    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = ""
    print("You: " +you)
    # Understand
    if you == "":
        robot_brain = "I cant hear you, try again"

    elif "hello" in you:
        robot_brain = "Hello Hong Hieu"

    elif  "today" in you:
        today = date.today()
        robot_brain = today.strftime("%B %d, %Y")
    elif "time" in you:
        now = datetime.now()
        robot_brain= now.strftime("%H hours %M minutes %S seconds")
    elif "president" in you:
        robot_brain = "Donald Trump!!"
    elif "bye" in you:
        robot_brain = "Bye Hong Hieu"
        print("Robot brain: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break

    else:
        robot_brain = "I'm fine thank you and you!"

    # print("Robot brain: "+ robot_brain)
    # # Speak
    # # robot_brain = "Hello Hong Hieu"
    # robot_mouth.say(robot_brain)
    #
    # # robot_mouth.say("I will speak this text, I am Hong Hieu, Currently I am AI Engineer at Aimesoft")
    # robot_mouth.runAndWait()

#text to speech:
# pyttsx3
# pip install speechrecognition
# pip install pyaudio