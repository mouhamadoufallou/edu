from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login as auth_login, logout, login
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

def index(request):
    return render(request, 'base/home.html')


def add_user(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = form.cleaned_data.get('is_admin')
            user.is_superuser = form.cleaned_data.get('is_admin')
            user.is_student = form.cleaned_data.get('is_student')
            user.is_teacher = form.cleaned_data.get('is_teacher')
            user.save()
            login(request, user)
            msg = 'Utilisateur créé et connecté'
            return redirect('/')
        else:
            msg = 'Le formulaire n\'est pas valide'
    else:
        form = SignUpForm()
    return render(request, 'accounts/add_user.html', {'form': form, 'msg': msg})

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                if user.is_admin:
                    return redirect('admin_dashboard')
                elif user.is_student:
                    return redirect('student_dashboard')
                elif user.is_teacher:
                    return redirect('teacher_dashboard')
            else:
                msg = 'Identifiants invalides'
        else:
            msg = 'Erreur de validation du formulaire'
    return render(request, 'accounts/login.html', {'form': form, 'msg': msg})

@login_required
def admin_dashboard(request):
    if not request.user.is_admin:
        raise PermissionDenied
    return render(request, 'base/base.html')

@login_required
def student_dashboard(request):
    if not request.user.is_student:
        raise PermissionDenied
    return render(request, 'base/base.html')

@login_required
def teacher_dashboard(request):
    if not request.user.is_teacher:
        raise PermissionDenied
    return render(request, 'base/base.html')

def user_logout(request):
    logout(request)
    return redirect("login_view")
