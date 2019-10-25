from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name='index.htm'


class AboutPageView(TemplateView):
    template_name = 'about.htm'



class ContactPageView(TemplateView):
    template_name = 'contact.htm'