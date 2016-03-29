from django import template
from django.db.models import get_model


register = template.Library()


@register.inclusion_tag("tags/DictSelect.html")
def DictSelect(dictcode,**kwargs):
    # FIXME 处理异常
    dict = get_model('DataDict', 'Dict').objects.get(dictcode=dictcode)
    dict_value = dict.item_set.all()
    select_id = kwargs.get('id',None)
    select_name = kwargs.get('name',None)
    select_class = kwargs.get('class',None)
    value = kwargs.get('value',None)
    
    return {
        'dict_value': dict_value,
        'select_id': select_id,
        'select_name': select_name,
        'select_class': select_class,
        'value': value
    }
