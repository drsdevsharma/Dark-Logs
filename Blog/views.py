from django.shortcuts import render,redirect
from .models import Post
from .forms import PostForm
from django.contrib import messages

# Create your views here.
def dashboard(request):
    if request.user.is_authenticated:
        blogs = Post.objects.filter(user=request.user)
        totalBlog = len(list(blogs))
        return render(request, 'dashboard.html' ,{'blogs':blogs,'totalBlog':totalBlog})
    else:
        return redirect('login')


def PostBlog(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            form = PostForm()
            return render(request, 'addblog.html', {'form': form,'title':'Add'})
        else:
            form = PostForm(request.POST)
            if form.is_valid():
                user = request.user
                title = form.cleaned_data['title']
                blog = form.cleaned_data['blog']
                blog = Post(user = user, title = title, blog = blog)
                blog.save()
                messages.success(request , 'Blog post added successfully')
            return redirect('dashboard')
    else:
        return redirect('login')


def UpdateBlog(request,id):
    if request.user.is_authenticated:
        blogpost = Post.objects.get(pk = id)
        if request.method == 'GET':
            form = PostForm(instance=blogpost)
            return render(request, 'addblog.html', {'form': form , 'title':'Update'})
        else:
            form = PostForm(request.POST,instance=blogpost)
            if form.is_valid():
                print (form)
                title = form.cleaned_data['title']
                blog = form.cleaned_data['blog']
                blogpost.title = title
                blogpost.blog = blog
                blogpost.save()
                messages.success(request , 'Blog post updated successfully')
            return redirect('dashboard')
    else:
        return redirect('login')


def DeleteBlog(request,id ):
    if request.method == 'POST':
        if request.user.is_authenticated:
            blogpost = Post.objects.get(pk = id)
            blogpost.delete()
            messages.success(request, 'Blog post deleted successfully')
            return redirect('dashboard')
        
