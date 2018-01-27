from django import template
from ..models import Post, Category

register = template.Library()

@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-time_created')[:num]

@register.simple_tag
def archives():
    return Post.objects.dates('time_created', 'month', order='DESC')


@register.simple_tag
def get_categories():
    return Category.objects.all()