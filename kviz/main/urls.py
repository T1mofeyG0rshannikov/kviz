from main.view.api import AnswerView, ClientView, CreateKvizView, GetClientsExcel, GetKvizCountView, LoginView
from main.view.views import Index, KvizView, VKView
from django.urls import path


urlpatterns = [
    path('', Index.as_view()),
    path('kviz', KvizView.as_view()),
    path('vk', VKView.as_view()),
    path('answer', AnswerView.as_view()),
    path('create-kviz', CreateKvizView.as_view()),
    path('client', ClientView.as_view()),
    path('file', GetClientsExcel.as_view()),
    path('login', LoginView.as_view()),
    path('kviz-count', GetKvizCountView.as_view()),
]
