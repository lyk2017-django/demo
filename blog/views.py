from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse

from blog.models import Entry


def anasayfa(request):
    return render(request, "blog/anasayfa.html",
                  {"isim": request.POST.get("isim")})


def list_entry(request):
    return render(request, "blog/listele.html",
                  {"entries": Entry.objects.filter(is_reported=False)})


def detail_entry(request, entry_id):
    entry = get_object_or_404(Entry, id=entry_id, is_reported=False)
    updates = []
    entry.reads += 1
    if "like" in request.POST:
        entry.likes += 1
        updates.append("likes")
    else:
        entry.likes += 1
        updates.append("reads")
    if "report" in request.POST:
        entry.is_reported = True
        updates.append("is_reported")
    entry.save(update_fields=updates)

    if "is_reported" in updates:
        return HttpResponseRedirect(redirect_to=reverse("listele"))
    return render(request, "blog/goster.html",
                  {"entry": entry})


