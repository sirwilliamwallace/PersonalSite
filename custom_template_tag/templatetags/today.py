from django import template
from datetime import datetime

register = template.Library()


@register.simple_tag(name="return_today")
def return_today():
    today = datetime.today().strftime('%Y/%m/%d')
    return today
