from django.shortcuts import render, HttpResponse

# Create your views here.


def render_main(request):
    text = f"""
    <h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <i>{name}</i>
    """
    return HttpResponse(text)

def render_about(request):
    text = f"""
    <p>
    <ul>
    Имя: Иван
    Отчество: Петрович
    Фамилия: Иванов
    телефон: 8-923-600-01-02
    email: vasya@mail.ru
    <p>
    """
    return HttpResponse(text)
