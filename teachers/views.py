from django.shortcuts import render, redirect, get_object_or_404
from teachers.forms import ProfesseurForm
from teachers.models import Professeur

# Create your views here.
def add_teacher(request):
    if request.method == "POST":
        form = ProfesseurForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                pass
    else:
        form = ProfesseurForm()
    return render(request, 'teachers/add_teacher.html', {'form': form})

def show_teacher(request):
    professeurs = Professeur.objects.all()
    return render(request, "teachers/show_teacher.html", {'professeurs': professeurs})

def edit_teacher(request, id):
    professeur = Professeur.objects.get(id=id)
    return render(request, 'teachers/edit_teacher.html', {'professeur': professeur})

def update_teacher(request, id):
    professeur = Professeur.objects.get(id=id)
    form = ProfesseurForm(request.POST, instance=professeur)
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request, 'teachers/edit_teacher.html', {'professeur': professeur})

def destroy_teacher(request, id):
    professeur = Professeur.objects.get(id=id)
    professeur.delete()
    return redirect("/")

# New detail_teacher function
def detail_teacher(request, id):
    teacher = get_object_or_404(Professeur, id=id)
    return render(request, 'teachers/detail_teacher.html', {'teacher': teacher})
