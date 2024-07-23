from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def index(request):
    return render(request, 'index.html')


def add_user(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'Utilisateur créé'
            return redirect('/')
        else:
            msg = 'Le formulaire n\'est pas valide'
    else:
        form = SignUpForm()
    return render(request,'accounts/add_user.html', {'form': form, 'msg': msg})

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('home')
            elif user is not None and user.is_student:
                login(request, user)
                return redirect('student')
            elif user is not None and user.is_teacher:
                login(request, user)
                return redirect('teacher')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'accounts/login.html', {'form': form, 'msg': msg})


def admin(request):
    return render(request,'admin.html')


def student(request):
    return render(request,'students/student.html')


def teacher(request):
    return render(request,'teachers/teacher.html')

def user_logout(request):
    logout(request)
    return redirect("login_view")