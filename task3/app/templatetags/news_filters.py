from django import template
from datetime import datetime


register = template.Library()


@register.filter
def format_date(value):
    now = datetime.now()
    then = datetime.fromtimestamp(value)
    delta = now - then
    minute = 60
    hour = 60*60
    if delta.seconds < 10*minute:
        return 'Только что'
    elif delta.seconds < 24*hour:
        return f'{delta.seconds // hour} часов назад'
    else:
        return then


@register.filter
def set_score(value, default):
    if value:
        v = int(value)
        if v <= -5:
            return 'все плохо'
        elif -5 < v < 5:
            return 'нейтрально'
        else:
            return 'хорошо'
    else:
        d = str(default)
        return d


@register.filter
def format_num_comments(value):
    v = int(value)
    if v == 0:
        return 'Оставьте комментарий'
    elif 0 < v <= 50:
        return value
    else:
        return '50+'


@register.filter
def count_view(value, count):
    li = value.split()
    start_count = li[0:count]
    finish_count = li[-count:]
    text = f'{" ".join(start_count)} . . . {" ".join(finish_count)}'
    return text

