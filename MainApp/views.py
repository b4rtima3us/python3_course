from MainApp import settings
from django.shortcuts import render, HttpResponse

# Create your views here.

items = [
   {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
   {"id": 2, "name": "Куртка кожаная", "quantity": 2},
   {"id": 5, "name": "Coca-cola 1 литр", "quantity": 12},
   {"id": 7, "name": "Картофель фри", "quantity": 0},
   {"id": 8, "name": "Кепка", "quantity": 124},
]


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
    context = {
        'title': 'Items',
        'items': items
    }
    return render(request, 'items.html', context)


def render_item_by_id(request, item_id):
    item = next((i for i in items if i['id'] == item_id), None)
    if item:
        context = {
            'title': 'Item',
            'item': item
        }
        return render(request, 'item.html', context)
    context = {
        'title': 'Error',
        'item': f'Товар с id={item_id} не найден'
    }
    return render(request, 'errors.html', context)

