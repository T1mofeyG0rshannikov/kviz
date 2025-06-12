from main.view.api import AnswerView, CreateKvizView, GetClientsExcel
from main.view.views import Index, KvizView, VKView
from django.urls import path


urlpatterns = [
    path('', Index.as_view()),
    path('kviz', KvizView.as_view()),
    path('vk', VKView.as_view()),
    path('answer', AnswerView.as_view()),
    path('kviz', CreateKvizView.as_view()),
    path('file', GetClientsExcel.as_view())
]
