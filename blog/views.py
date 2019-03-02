from django.shortcuts import render

# from django.http import HttpResponse

posts =[
    {
        'author':'sam',
        'title':'Blog Post 1',
        'content':'First Post 1',
        'date_posted': 'August 28 2018'
    },
{
        'author':'Tom',
        'title':'Blog Post 2',
        'content':'Second Post ',
        'date_posted': 'August 29 2018'
    }
]


def home(request):
    context={
        'posts':posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html',{'title':'About'})

