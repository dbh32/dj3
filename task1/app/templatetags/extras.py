from django import template
from app.views import inflation_view

register = template.Library()


@register.filter(name='color')
def cell_color(value):
    try:
        if float(value) < 0:
            return '#008000'
        elif 0 <= float(value) < 1:
            return '#FFFFFF'
        elif 1 <= float(value) < 2:
            return '#E9967A'
        elif 2 <= float(value) < 5:
            return '#FF0000'
        elif 5 <= float(value):
            return '#800000'
    except:
        return '#FFFFFF'


@register.filter(name='none')
def if_none(value):
    if value != '':
        return value
    else:
        return '-'
