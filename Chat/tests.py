from django.test import TestCase
import en_core_web_sm

nlp = en_core_web_sm.load()
# Create your tests here.

from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

chatbot = ChatBot("Ron Obvious")
conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

trainer = ListTrainer(chatbot)

trainer.train(conversation)
response = chatbot.get_response("Good morning!")
print(response)