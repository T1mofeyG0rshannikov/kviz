from main.views import AnswerView, CreateKvizView, Index
from django.urls import path

urlpatterns = [
    path('', Index.as_view()),
    path('answer', AnswerView.as_view()),
    path('kviz', CreateKvizView.as_view())
]
