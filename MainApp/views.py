from MainApp.models import Item
from MainApp import settings
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist


def render_main(request):
    return render(request, 'index.html')


def render_about(request):
    context = {
        'name': settings.USER_NAME,
        'middle_name': settings.USER_MIDDLE_NAME,
        'surname': settings.USER_SURNAME,
        'phone': settings.USER_PHONE,
        'email': settings.USER_EMAIL
    }
    return render(request, 'about.html', context)


def render_items(request):
    items = Item.objects.all()
    context = {'items': items}
    return render(request, 'items.html', context)


def render_item_by_id(request, item_id):
    try:
        item = Item.objects.get(id=item_id)
        context = {
            'title': 'Item',
            'item': item
        }
        return render(request, 'item.html', context)
    except ObjectDoesNotExist:
        context = {
            'title': 'Error',
            'item': f'Товар с id={item_id} не найден'
        }
        return render(request, 'errors.html', context)

