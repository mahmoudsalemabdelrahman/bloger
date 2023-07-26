from django.shortcuts import render, get_object_or_404
from blog.models import Post, Comment
from .forms import NewComment

# Create your views here.


def home(request):
    context ={
        'title':'الصفحه الرئيسيه',
        'posts':Post.objects.all()
    }
    return render(request ,'blog/index.html',context)

def about(request):
        return render(request, 'blog/about.html' ,{'title':'من أنا'})


def post_detail (request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        comments = post.comments.filter(active=True)
        # check before save data from comment form
        if request.method =='POST':
               comment_form =NewComment(data=request.POST)
               if comment_form.is_valid():
                      new_comment = comment_form.save(commit=False)
                      new_comment.post = post
                      new_comment.save()
                      comment_form = new_comment()       
        else:
               comment_form = NewComment()
        context ={
            'title':post,
            'post': post,
            'comments':comments,
            'comment_form':comment_form,
        }
        
        return render(request, 'blog/detail.html', context)
