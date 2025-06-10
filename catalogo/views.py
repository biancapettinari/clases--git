from django.shortcuts import render
from .models import Libro

from .forms import AutorForm, EditorialForm, LibroForm
from django.shortcuts import redirect



def index(request):
    libros = Libro.objects.all()
    return render(request, "catalogo/index.html", {"libros": libros})


# Formulario para autor
def crear_autor(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = AutorForm()
    return render(request, "catalogo/formulario.html", {"form": form, "titulo": "Agregar Autor"})

# Formulario para editorial
def crear_editorial(request):
    if request.method == "POST":
        form = EditorialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = EditorialForm()
    return render(request, "catalogo/formulario.html", {"form": form, "titulo": "Agregar Editorial"})


# Formulario para libro
def crear_libro(request):
    if request.method == "POST":
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = LibroForm()
    return render(request, "catalogo/formulario.html", {"form": form, "titulo": "Agregar Libro"})


# Formulario de búsqueda

def buscar_libro(request):
    query = request.GET.get("q", "")
    resultados = Libro.objects.filter(titulo__icontains=query) if query else []
    return render(request, "catalogo/buscar.html", {"resultados": resultados, "query": query})
