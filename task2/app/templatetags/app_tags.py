from django import template

register = template.Library()


@register.filter(name='if_active')
def check_if_active(value, page_name):
    if value == page_name:
        ca = 'class = active'
        return ca
