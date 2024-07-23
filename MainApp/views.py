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
    table = '<ol type="1">'
    for i in items:
        table += f'<li><a href="{i["id"]}">{i["name"]}</a> : {i["quantity"]}</li>'
    table += '</ol>'
    return HttpResponse(table)


def render_item_by_id(request, item_id):
    item = next((i for i in items if i['id'] == item_id), None)
    if item:
        response = f"""
        {item['name']}: {item['quantity']}
        """
    else:
        response = f'Товар с id={item_id} не найден'
    response += f'<br><a href="/items">Назад к списку товаров</a>'
    return HttpResponse(response)
