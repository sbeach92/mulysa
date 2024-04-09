from django import template

register = template.Library()

@register.filter
def strip(text):
    """
    Remove trailing newlines from text
    """
    return text.strip()
