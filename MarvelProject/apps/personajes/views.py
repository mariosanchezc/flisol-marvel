from django.shortcuts import render
import datetime


def prueba1(request):
    """
    Permite renderizar mi Primer template
    """
    title = "Este es mi Primer Template"
    date = datetime.datetime.now()
    template_name = 'personajes/index.html'
    return render(request, template_name, context={"title": title, 'date': date})