from django.shortcuts import render
from django.views.generic import View, ListView, DetailView, UpdateView
from django.http import HttpResponseRedirect
from .forms import PersonajeForm
from .models import Personaje
import datetime


def prueba1(request):
    """
    Permite renderizar mi Primer template
    """
    title = "Este es mi Primer Template"
    date = datetime.datetime.now()
    template_name = 'personajes/index.html'
    return render(request, template_name, context={"title": title, 'date': date})


class CreatePersonajeView(View):
    """
    Permite crear un nuevo personaje de Marvel
    """
    template_name = 'personajes/crear.html'
    form_class = PersonajeForm

    def get(self, request, *args, **kwargs):
        """
        Visualiza el template
        """
        title = "Creación de un personaje Marvel"
        tipos = ["HEROE", "VILLANO"]
        return render(request, self.template_name, context={
            'title': title, 'form':self.form_class,
            'tipos': tipos})

    def post(self, request, *args, **kwargs):
        """
        Crea un nuevo Personaje
        """
        form = PersonajeForm(request.POST, request.FILES)
        if form.is_valid():
            personaje = Personaje(
                nombre=form.cleaned_data['nombre'],
                imagen=form.cleaned_data['imagen'],
                descripcion=form.cleaned_data['descripcion'],
                tipo_personaje=form.cleaned_data['tipo_personaje'],
            )
            personaje.save()
            return HttpResponseRedirect("/list-personajes")
        return render(request, self.template_name, {"form": form})


class ListPersonajeView(ListView):
    """
    Lista todos los Personajes de Marvel
    """
    template_name = 'personajes/list-personaje.html'
    model = Personaje
    paginate_by = 100


    def get_queryset(self):
        return Personaje.objects.all().order_by('-fecha_creacion')


class PersonajeDetail(DetailView):
    """
    Detalla Nuestro Personaje
    """
    template_name = 'personajes/detail-personaje.html'
    model = Personaje


class PersonajeUpdateView(UpdateView):
    """
    Permite actualizar un Personaje
    """
    template_name = 'personajes/update-personaje.html'
    model = Personaje
    fields = ['nombre', 'tipo_personaje', 'descripcion', 'imagen']
