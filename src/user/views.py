from django.shortcuts import render, redirect
from .forms import UserCreationForms
from django.contrib import messages

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
