import requests
import speech_recognition as sr

from time import ctime
import time
import pyttsx3
from ChatBotProject.config import *


import io
import random
import string # to process standard python strings
import warnings
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
warnings.filterwarnings('ignore')

import nltk
from nltk.stem import WordNetLemmatizer
#Reading in the dataset
with open('chatbot2.txt','r', encoding='utf8', errors ='ignore') as fin:
    raw = fin.read().lower()

# TOkenisation
sent_tokens = nltk.sent_tokenize(raw)# converts to list of sentences
word_tokens = nltk.word_tokenize(raw)# converts to list of words

# Preprocessing
lemmer = WordNetLemmatizer()
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

print(STATUS)


# Generating response
def response(user_response):

    robo_response=''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo_response=robo_response+"I am sorry! i am not trained to answer that"
        # print("robo resp ", robo_response)
        return robo_response
    else:
        # print(11)
        robo_response = robo_response+sent_tokens[idx]
        # print(12)
        # print("robo resp >",robo_response)
        return robo_response


def speak(audioString):
    print(audioString)

    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-70)
    engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")

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
        speak("excuse me")
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

    elif "next train" in data:
        message = "Next train is shornour nilamboor road passenger"
        print(MESSAGE," : ",message)
        speak(message)
        voiceMessage("next train",message)

    elif "platform" in data:
        message = " third platform"
        print(MESSAGE, " : ", message)
        speak(message)
        voiceMessage("platform",message)


    elif "hello" in data:
        message = "yes i am listening"
        print(MESSAGE, " : ", message)
        speak(message)
        voiceMessage("hello",message)
    elif "name" in data:
        message = "My name is jasi version 1.0 developed as a prototype"
        print(MESSAGE, " : ", message)
        speak(message)
        voiceMessage("name",message)
    elif "say something" in data:
        message = "One day i will become something"
        print(MESSAGE, " : ", message)
        speak(message)
        voiceMessage("say something",message)
    elif "what is your name" in data:
        message = "My name is jasi version 1.0 developed as a prototype"
        print(MESSAGE, " : ", message)
        speak(message)
        voiceMessage("what is your name",message)
    elif "who created you" in data:
        message = "Mohamed jasir created me"
        print(MESSAGE, " : ", message)
        speak(message)
        voiceMessage("who created you",message)
    elif "you work for" in data:
        message = "Jasir"
        print(MESSAGE, " : ", message)
        speak(message)
        voiceMessage("you work for",message)
    elif "what is your aim" in data:
        message = "my aim is to build a better tomorrow"
        print(MESSAGE, " : ", message)
        speak(message)
        voiceMessage("what is your aim",message)
    elif "how are you" in data:
        message = "I am fine"
        print(MESSAGE, " : ", message)
        speak(message)
        voiceMessage("how are you",message)
    elif "bye" in data:
        message = "ok see ya"
        print(MESSAGE, " : ", message)
        speak(message)
        voiceMessage("bye",message)
        return True

    elif "what time is it" in data:

        speak(ctime())
        # speak(message)
        # voiceMessage(message)

    # elif "where is " in data:
    #
    #     data = data.split(" ")
    #     location = data[2]
    #     print("Location :",location)
    #     speak(location+ ' is some where on the earth')
    #
    else:
        print("else worked")
        replay = response(data)
        speak(replay)
        voiceMessage(data,replay)


def voiceMessage(yourmessage,message):
    print("you>",yourmessage)
    print("GAB>",message)
    API_ENDPOINT = URL+"chat/"

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
