from main.views import AnswerView, CreateKvizView, GetClientsExcel, Index, IndexVK
from django.urls import path

urlpatterns = [
    path('', Index.as_view()),
    path('vk', IndexVK.as_view()),
    path('answer', AnswerView.as_view()),
    path('kviz', CreateKvizView.as_view()),
    path('file', GetClientsExcel.as_view())
]
