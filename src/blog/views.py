from django.shortcuts import render
from blog.models import Post


# Create your views here.


def home(request):
    context ={
        'title':'الصفحه الرئيسيه',
        'posts':Post.objects.all()
    }
    return render(request ,'blog/index.html',context)

def about(request):
        return render(request, 'blog/about.html' ,{'title':'من أنا'})
