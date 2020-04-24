from django.conf.urls import url
from django.urls import path, include
from Chat import views
urlpatterns = [
    path('',views.ChatView.as_view()),
    path('speak/',views.SpeakMessage.as_view()),
    path('questions/',views.GetQuestions.as_view()),
]