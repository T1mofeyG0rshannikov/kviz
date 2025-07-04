from main.forms.get_forms import get_forms
from main.models import Client
from django.views.generic import TemplateView

from seo.models import IndexPage


class KvizView(TemplateView):
    template_name = 'main/kviz.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client_id = self.request.GET.get("client")
        if client_id:
            context["client"] = Client.objects.get(id=int(client_id))

        messanger = self.request.GET.get("messanger")

        context['messanger'] = messanger
        context["settings"] = IndexPage.objects.first()

        context["forms"] = get_forms()

        return context


class Index(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["settings"] = IndexPage.objects.first()

        return context


class VKView(KvizView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["messanger"] = "vk"

        return context
