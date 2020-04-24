from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView
from rest_framework.response import Response



#Meet Robo: your friend

#import necessary libraries
import io
import random
import string # to process standard python strings
import warnings
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings

from Chat.models import Questions
from Chat.serializers import QuestionsSerializer

warnings.filterwarnings('ignore')

import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('popular', quiet=True) # for downloading packages

# uncomment the following only the first time
#nltk.download('punkt') # first-time use only
#nltk.download('wordnet') # first-time use only

import pyttsx3

#Reading in the corpus


def bot(message):
    with open('chatbot2.txt', 'r', encoding='utf8', errors='ignore') as fin:
        raw = fin.read().lower()

    # TOkenisation
    sent_tokens = nltk.sent_tokenize(raw)  # converts to list of sentences
    word_tokens = nltk.word_tokenize(raw)  # converts to list of words

    # Preprocessing
    lemmer = WordNetLemmatizer()

    def LemTokens(tokens):
        return [lemmer.lemmatize(token) for token in tokens]

    remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

    def LemNormalize(text):
        return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

    # Keyword Matching
    GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey",)
    GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]

    def greeting(sentence):
        """If user's input is a greeting, return a greeting response"""
        for word in sentence.split():
            if word.lower() in GREETING_INPUTS:
                return random.choice(GREETING_RESPONSES)

    # Generating response
    def response(user_response):
        robo_response = ''
        sent_tokens.append(user_response)
        TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
        tfidf = TfidfVec.fit_transform(sent_tokens)
        vals = cosine_similarity(tfidf[-1], tfidf)
        idx = vals.argsort()[0][-2]
        flat = vals.flatten()
        flat.sort()
        req_tfidf = flat[-2]
        if (req_tfidf == 0):
            robo_response = robo_response + "I am sorry! I cant answer that"
            return robo_response
        else:
            robo_response = robo_response + sent_tokens[idx]
            return robo_response

    flag = True
    print("Gabot: Hi how can i help you. say bye if you done with me !")
    # while (flag == True):
    # user_response = input()
    user_response = message
    user_response = user_response.lower()
    print("You > ", user_response)
    if (user_response != 'bye'):
        if (user_response == 'thanks' or user_response == 'thank you'):
            flag = False
            robot = "You are welcome.."

            print("ROBO > You are welcome..")
            return robot
        else:
            if (greeting(user_response) != None):
                print("ROBO > " + greeting(user_response))
                robot = greeting(user_response)
                return robot
            else:
                robot = response(user_response)
                print("ROBO >", robot)
                sent_tokens.remove(user_response)
                return robot
    else:
        flag = False
        robot = "Bye! take care.."
        print("Bye! take care..")
    return robot

def speak(audioString):
    print(audioString)

    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    volume = engine.getProperty('volume')
    voice = engine.getProperty('voice')

    # print('default')
    # print('default rate',rate)
    # print("volume",volume)
    # print("voice",voice)
    # engine.say(audioString)
    # engine.runAndWait()

    print('Modified')

    engine.setProperty('rate', rate-70)
    rate = engine.getProperty('rate')
    volume = engine.getProperty('volume')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
    # for voice in voices:
    #     print("Voice id : ",voice.id)
    #     engine.setProperty('voice', voice.id)
    #     engine.say('The quick brown fox jumped over the lazy dog.')

    # print('modified')
    # print('rate', rate)
    # print("volume", volume)
    # print("voice", voice)
    # print("voices", voices)

    engine.say(audioString)
    engine.runAndWait()

class ChatView(ListAPIView):
    def post(self,request):
        message = self.request.POST.get('message')
        response = bot(message)
        # speak(response)

        return Response({
            "status":True,
            "You":message,
            "Gabot":response
        })

class SpeakMessage(ListAPIView):
    def post(self,request):
        message = self.request.POST.get('message')
        speak(message)

        return Response({
            "status":True,
            "You":message,
        })

class GetQuestions(ListAPIView):

    serializer_class = QuestionsSerializer
    def get_queryset(self):
        keyword = self.request.GET['keyword']
        id = self.request.GET['id']
        parent_id = self.request.GET['parent_id']
        print(keyword)
        if keyword=="parent":
            qeuryset = Questions.objects.filter(parent=True)
        elif keyword=="all":
            qeuryset = Questions.objects.all()
        else:
            qeuryset = Questions.objects.filter(parent=False)

        if id:
            qeuryset = Questions.objects.filter(id=id)
        if parent_id:
            qeuryset = Questions.objects.filter(child__id=parent_id)
        return qeuryset