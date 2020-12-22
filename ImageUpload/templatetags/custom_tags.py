from django import template
from static.util.cal import *

register = template.Library()


@register.filter(name='return_name_haksik')
def return_name(value):
    return get_name_haksik(int(value))


@register.filter(name='return_name_meal')
def return_name_meal(value):
    return get_name_meal(int(value))
