from django.shortcuts import render,redirect
from .forms import RegisterationForm
from django.contrib import messages
from Blog.models import Post

# Create your views here.
def home(request):
    blogs = Post.objects.all()
    return render(request, 'home.html' ,{'blogs': blogs})


def about(request):
    return render(request, 'about.html')


def RegisterUser(request):
    if request.method == 'GET':
        form = RegisterationForm()
        return render(request,'register.html', {'form':form})
    else:
        form = RegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'User registered successfully ')
            return redirect('/')
        return render(request, 'register.html', {'form': form})



