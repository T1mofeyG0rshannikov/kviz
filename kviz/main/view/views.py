from main.forms.get_forms import get_forms
from main.models import Kviz
from django.views.generic import TemplateView

from seo.models import IndexPage


class KvizView(TemplateView):
    template_name = 'main/kviz.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        kviz_id = self.request.GET.get("kviz")
        kviz = Kviz.objects.get(id=int(kviz_id))

        context["kviz"] = kviz
        context["settings"] = IndexPage.objects.first()

        context["forms"] = get_forms()

        return context


class Index(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["settings"] = IndexPage.objects.first()
        

        return context


class VKView(TemplateView):
    template_name = 'main/index_vk.html'
