from django.http import HttpResponse
from django.views import View
from main.view.api import AnswerView, CreateKvizView, GetClientsExcel
from main.view.views import Index, KvizView, VKView
from django.urls import path
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from django.utils.decorators import method_decorator
from django.contrib.auth.models import User


@method_decorator(csrf_exempt, name="dispatch")
class LoginView(View):
    def post(self, request):
        user = User.objects.get(username=request.POST["username"])
        if user.check_password(request.POST["password"]):
            return HttpResponse(status=200)
        
        return HttpResponse(status=401)


urlpatterns = [
    path('', Index.as_view()),
    path('kviz', KvizView.as_view()),
    path('vk', VKView.as_view()),
    path('answer', AnswerView.as_view()),
    path('create-kviz', CreateKvizView.as_view()),
    path('file', GetClientsExcel.as_view()),
    path('login', LoginView.as_view())
]
