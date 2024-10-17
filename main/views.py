from django.shortcuts import render

def index(request):
    context = {
        'title': 'Главная страница',
        'products': ['Жвачка по рублю', 'Кока-коля', 'Чипсы «Лейс»'],
    }
    return render(request, 'main/index.html', context)

def contacts(request):
    context = {
        'title': 'Контактная информация',
    }
    return render(request, 'main/contacts.html', context)