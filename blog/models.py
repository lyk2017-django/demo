from django.db import models
from django.conf import settings

# Create your models here.


class Entry(models.Model):
    title = models.CharField(max_length=160)
    body = models.TextField()
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    tags = models.ManyToManyField("Tag", blank=True)
    award = models.OneToOneField("Award", null=True, blank=True)
    reads = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    is_reported = models.BooleanField(default=False)


class Tag(models.Model):
    name = models.CharField(max_length=40)


class Award(models.Model):
    name = models.CharField(max_length=40)
