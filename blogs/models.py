from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True)
    
    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True)
    
    def __str__(self):
        return self.name


class Post(models.Model):
    title    = models.CharField(max_length=255, blank=False, null=False)
    body     = models.TextField(blank=True, null=False)
    created  = models.DateTimeField(auto_now_add=True, editable=False, blank=False, null=False)
    updated  = models.DateTimeField(auto_now=True, editable=False, blank=False, null=False)
    user     = models.ForeignKey('customusers.User', on_delete=models.CASCADE, default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags     = models.ManyToManyField(Tag,blank=True)

    def __str__(self):
        return self.title