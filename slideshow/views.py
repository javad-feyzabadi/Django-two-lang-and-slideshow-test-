from django.shortcuts import render,redirect
from django.utils.translation import activate
from . models import SlideShow
from django.contrib.auth import logout  

def home(request):
    context = {
        'slides':SlideShow.objects.filter(status = True,article__status = True)
    }
    return render(request,'slideshow/home.html',context)

def change_lang(request):
    activate(request.GET.get('lang'))
    return redirect(request.GET.get('next'))

def logout_view(request):
    logout(request)
    return redirect(request.GET.get('next'))
