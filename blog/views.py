from django.shortcuts import render

# Create your views here.

def anasayfa(request):
    return render(request, "blog/anasayfa.html")