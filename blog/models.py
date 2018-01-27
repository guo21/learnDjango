from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=60)
    body = models.TextField()
    time_created = models.DateTimeField()
    time_last_modified = models.DateTimeField()
    body_abstract = models.CharField(max_length=300,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-time_created']