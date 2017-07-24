from django.conf.urls import url
from .views import *

urlpatterns = [
    url("^$", anasayfa, name="home"),
    url("^list$", list_entry, name="listele"),
]
