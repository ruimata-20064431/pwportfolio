
from django import template

register = template.Library()


@register.filter
def set_size(text, size = 1):
    str_aux = ''.join(['&nbsp;' for x in range(size)])
    
    result = (''.join(str(text)) + str_aux)[:size] + ' | '
    print(str(len(result)) + ":'" + result + "'")

    return (''.join(str(text)) + str_aux)[:size] + ' | '

register.filter("set_size", set_size )