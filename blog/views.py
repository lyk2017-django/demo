from django.shortcuts import render

# Create your views here.

from blog.models import Entry


def anasayfa(request):
    return render(request, "blog/anasayfa.html",
                  {"isim": request.POST.get("isim")})


def list_entry(request):
    return render(request, "blog/listele.html",
                  {"entries": Entry.objects.filter(is_reported=False)})


