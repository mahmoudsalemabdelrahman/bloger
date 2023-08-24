from django.shortcuts import render, redirect
from .forms import UserCreationForms, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from blog.models import Post

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForms(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'تهانينا{username} لقد تم التسجيل بنجاح')
            return redirect('home')
    else:
        form = UserCreationForms()
    return render(request, 'user/register.html', {
        'title': 'التسجيل',
        'form':form,
    })
def login_user(request):
    if request.method == 'POST':
        form = LoginForm()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, 'هناك خطا في اسم المستخدم او كلمه المرور')
    else:
        form =LoginForm()
    return render(request, 'user/login.html', {
        'title':'تسجيل الدخول',
        'form':form,
    })
def logout_user(request):
    logout(request)
    return render(request , 'user/logout.html' ,{
        'title':' تسجيل الخروج'
    })
def profile(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, 'user/profile.html', {
        'title': 'الملف الشخصي',
        'posts': posts,
    })