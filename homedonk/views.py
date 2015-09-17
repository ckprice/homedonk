from django.http import HttpResponse
from django.template import RequestContext, loader


def home(request):
    template = loader.get_template('home/home.html')
    return HttpResponse(template.render())