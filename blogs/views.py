from django.shortcuts import render
from .models import Posts

# Create your views here.
def getBlogs(request):
    try:
        allBlogs = []
        blogs = Posts.objects.all().values()
        for blog in blogs:
            blog['thumbnail'] = str(blog['thumbnail'])
            allBlogs.append(blog)
        return render(request, 'blogs.html', {"allBlogs":allBlogs})
    except Exception as e:
        raise e

def getBlog(request, slug):
    try:
        allBlogs = []
        data = Posts.objects.filter(slug=slug).values()
        others = Posts.objects.filter(~Q(slug=slug))[0:10].values()
        for i in data:
            content = i['content']
        for other in others:
            other['thumbnail'] = str(other['thumbnail'])
            allBlogs.append(other)
        return render(request, 'blog.html', {'blogs' : content, "allBlogs":allBlogs})
    except Exception as e:
        raise e