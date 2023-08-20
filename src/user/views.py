from django.shortcuts import render
from .forms import UserCreationForms

# Create your views here.
def register(request):
    form = UserCreationForms()
    return render(request, 'user/register.html', {
        'title': 'التسجيل',
        'form':form,
    })
