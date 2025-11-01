from django import template
from main.models import Category

register = template.Library()

@register.inclusion_tag("main/category_tags.html")
def show_categories():
    categories = Category.objects.all()
    return {'categories': categories}