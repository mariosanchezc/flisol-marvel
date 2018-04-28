from django.shortcuts import render
from django.views.generic import View
import datetime


def prueba1(request):
    """
    Permite renderizar mi Primer template
    """
    title = "Este es mi Primer Template"
    date = datetime.datetime.now()
    template_name = 'personajes/index.html'
    return render(request, template_name, context={"title": title, 'date': date})


class PruebaView(View):
    """
    Permite Crear una nueva Plantilla
    utilizan una vista basada en clase
    """
    template_name = 'personajes/index.html'

    def get(self, request, *args, **kwargs):
        """
        visualiza el template
        """
        title = "Este es mi Segundo Template"
        date = datetime.datetime.now()
        return render(request, self.template_name, context={'title': title, 'date':date})