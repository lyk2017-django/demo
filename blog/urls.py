from django.conf.urls import url
from .views import *

urlpatterns = [
    url("^$", anasayfa, name="home"),
    url("^list$", list_entry, name="listele"),
    url("^show/(?P<entry_id>\d+)/$", detail_entry, name="goster")
]
