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


# Keyword Matching
GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey",)
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]

def greeting(sentence):
    """If user's input is a greeting, return a greeting response"""
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


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
        robo_response=robo_response+"I am sorry! I cant answer that"
        # print("robo resp ", robo_response)
        return robo_response
    else:
        # print(11)
        robo_response = robo_response+sent_tokens[idx]
        # print(12)
        # print("robo resp >",robo_response)
        return robo_response


flag=True
print("Gabot: Hi how can i help you. say bye if you done with me !")
while(flag==True):
    user_response = input()
    user_response=user_response.lower()
    print("You > ", user_response)
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' ):
            flag=False

            print("Gabot > You are welcome..")
        else:
            if(greeting(user_response)!=None):
                print("Gabot > "+greeting(user_response))
            else:
                print("Gabot > ",end="")
                # print(1)
                print(response(user_response))
                # print(2)

                sent_tokens.remove(user_response)
    else:
        flag=False
        print("Gabot > Bye! take care..")

        

