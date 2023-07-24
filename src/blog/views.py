from django.shortcuts import render

# Create your views here.

posts =[ 
    {
        'title':'التدوينه الاولي',
        'content':'نص التدوينه الاولي تجريببي',
        'post_date':'15-3-2019',
        'author':'Mahmoud Salem',
    },
        {
        'title':'التدوينه الثانيه',
        'content':'نص التدوينه الثانيه تجريببي',
        'post_date':'28-3-2019',
        'author':'mohamed Ali',
    },
        {
        'title':'التدوينه الثالثه',
        'content':'نص التدوينه الثالثه تجريببي',
        'post_date':'15-3-2019',
        'author':'Ali Salem',
    },
        {
        'title':'التدوينه الرابعه',
        'content':'نص التدوينه الرابعه تجريببي',
        'post_date':'15-3-2019',
        'author':'Mazen Ibrahem',
    }
]
def home(request):
    context ={
        'title':'الصفحه الرئيسيه',
        'posts':posts
    }
    return render(request ,'blog/index.html',context)

def about(request):
        return render(request, 'blog/about.html' ,{'title':'من أنا'})
