import requests
import speech_recognition as sr

from time import ctime
import time
import pyttsx3
from ChatBotProject.config import *

print(STATUS)



def speak(audioString):
    print(audioString)

    engine = pyttsx3.init()
    engine.say(audioString)
    engine.runAndWait()

    # tts.save("audio.mp3")
    # os.system("pip audio.mp3")

def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    r.energy_threshold = 300
    with sr.Microphone() as source:
        print("Say something!")
        # print("source ",source)
        audio = r.listen(source)
        print("audio ",audio)

        # if not audio:
        #     print("Say ")

    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        speak("i did not understand")
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return data

def jarvis(data):

    if "check" in data:
        message = "what you want to check"
        print(MESSAGE," : ",message)
        speak(message)
        voiceMessage("check",message)

    if "next train" in data:
        message = "Next train is shornour nilamboor road passenger"
        print(MESSAGE," : ",message)
        speak(message)
        voiceMessage("next train",message)

    if "platform" in data:
        message = " third platform"
        print(MESSAGE, " : ", message)
        speak(message)
        voiceMessage("platform",message)


    if "hello" in data:
        message = "yes i am listening"
        print(MESSAGE, " : ", message)
        speak(message)
        voiceMessage("hello",message)
    if "name" in data:
        message = "My name is jasi version 1.0 developed as a prototype"
        print(MESSAGE, " : ", message)
        speak(message)
        voiceMessage("name",message)
    if "say something" in data:
        message = "One day i will become something"
        print(MESSAGE, " : ", message)
        speak(message)
        voiceMessage("say something",message)
    if "what is your name" in data:
        message = "My name is jasi version 1.0 developed as a prototype"
        print(MESSAGE, " : ", message)
        speak(message)
        voiceMessage("what is your name",message)
    if "who created you" in data:
        message = "Mohamed jasir created me"
        print(MESSAGE, " : ", message)
        speak(message)
        voiceMessage("who created you",message)
    if "you work for" in data:
        message = "Jasir"
        print(MESSAGE, " : ", message)
        speak(message)
        voiceMessage("you work for",message)
    if "what is your aim" in data:
        message = "my aim is to build a better tomorrow"
        print(MESSAGE, " : ", message)
        speak(message)
        voiceMessage("what is your aim",message)
    if "how are you" in data:
        message = "I am fine"
        print(MESSAGE, " : ", message)
        speak(message)
        voiceMessage("how are you",message)
    if "bye" in data:
        message = "ok see ya"
        print(MESSAGE, " : ", message)
        speak(message)
        voiceMessage("bye",message)
        return True

    if "what time is it" in data:

        speak(ctime())
        # speak(message)
        # voiceMessage(message)

    if "where is " in data:

        data = data.split(" ")
        location = data[2]
        print("Location :",location)
        speak(location+ ' is some where on the earth')
        # speak("Hold on Frank, I will show you where " + location + " is.")
        # os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")
        # os.system("chrome https://www.google.nl/maps/place/" + location + "/&amp;")

def voiceMessage(yourmessage,message):
    API_ENDPOINT = URL+"detect/"

    data = {
        "bot": message,
        "you": yourmessage,
        KEY:"voice"
    }
    # r = requests.post(url=API_ENDPOINT, data=data)

# initialization
time.sleep(2)
# speak("Hi Jasir, what can I do for you?")
print("Hi Jasir, what can I do for you?")
while 1:
    data = recordAudio()
    exit = jarvis(data)
    print("exit ? ",exit)
    if exit:
        break
