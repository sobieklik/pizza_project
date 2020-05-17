from django.template.defaulttags import register

@register.simple_tag
def add(a, b):
    return int(a) + int(b)

@register.simple_tag
def multiply(a, b):
    return int(a) * int(b)    

@register.filter(name='range') 
def times(number):
    return range(int(number))

