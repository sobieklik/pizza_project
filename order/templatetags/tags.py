
from django.template.defaulttags import register
import json

@register.simple_tag(name='json')
def json_dic(dictionary):
    return json.loads(dictionary)

@register.simple_tag
def get_sauces(dictionary, key):
    return dictionary.get(key,{}).get('sauce')

@register.simple_tag
def get_chips(dictionary, key):
    return dictionary.get(key,{}).get('chips')

@register.simple_tag
def get_meats(dictionary, key):
    return dictionary.get(key,{}).get('meat')        