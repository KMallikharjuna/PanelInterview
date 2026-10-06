from django.http import HttpResponse
from django.template import loader
def getProName(request):
    return HttpResponse("Welcome to DJango project")

def getHome(request):
    return HttpResponse(loader.get_template('Home.html').render())