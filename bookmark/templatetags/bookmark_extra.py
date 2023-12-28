from django import template

register = template.Library()


@register.filter(name='prange')
def page_range(value, arg):
    page_start = (value-1)//5*5+1
    page_end = page_start + 4

    if (value-1)//5 == (arg-1)//5:
        page_end = arg

    return list(range(page_start, page_end+1))

@register.filter(name='item_num')
def item_num(value, arg):
    item_num = (value-1)*5 + arg
    return item_num

@register.filter
def return_item(arr, _key):
    try:
        return arr[_key]
    except:
        return None