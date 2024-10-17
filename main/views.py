from django.shortcuts import render

def index(request):
    context = {
        'products': ['Жвачка по рублю', 'Кока-коля', 'Чипсы «Лейс»'],
    }
    return render(request, 'main/index.html', context)