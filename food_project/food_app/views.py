from django.shortcuts import render


def sign_up(request):
    return render(request, 'index.html')


def sign_in(request):
    return render(request, 'sign_in.html')
