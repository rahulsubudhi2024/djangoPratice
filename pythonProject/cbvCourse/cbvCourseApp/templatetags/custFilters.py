from django import template

register = template.Library()

@register.filter(name="myLower")
def custLower(value):
    if isinstance(value, str):
        return value[:3].lower()
    return value
