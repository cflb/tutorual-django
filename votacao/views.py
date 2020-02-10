from django.http import HttpResponse


def index(request):
    return HttpResponse("oiiiiiiiie")

def resultados(request):
    return HttpResponse('resultador')