from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class TemplateBasedCBV(TemplateView):
    template_name = 'hello.html'

class TemplateBasedCBV2(TemplateView):
    template_name = 'hello2.html'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'harish'
        context['marks'] = 100
        context['subject'] = 'python'
        return context
