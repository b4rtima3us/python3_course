from MainApp.models import Item
from MainApp import settings
from django.shortcuts import render, HttpResponse
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


def render_main(request):
    text = f"""
    <h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <i>{settings.USER_FULL_NAME}</i>
    """
    return render(request, 'index.html')


def render_about(request):
    text = f"""
    <p>
    Имя: {settings.USER_NAME} <br>
    Отчество: {settings.USER_MIDDLE_NAME} <br>
    Фамилия: {settings.USER_SURNAME} <br>
    Телефон: {settings.USER_PHONE} <br>
    Email: {settings.USER_EMAIL} <br>
    <p>
    """
    return HttpResponse(text)


def render_items(request):
    items = Item.objects.all()
    context = {
        'title': 'Items',
        'items': items
    }
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

