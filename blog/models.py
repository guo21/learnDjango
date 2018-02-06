import markdown
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
from django.utils.html import strip_tags


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
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})


    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def save(self, *args, **kwargs):
        if not self.body_abstract:
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            self.body_abstract = strip_tags(md.convert(self.body))[:54]

        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-time_created']


