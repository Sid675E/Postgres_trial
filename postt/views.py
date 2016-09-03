from django.http import HttpResponse

def index(response):
    return HttpResponse("<h1> Django unchained</h1>")
