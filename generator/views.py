from django.shortcuts import render
from django.http import HttpResponse
import random
def home(request):
    return render(request,'generator/home.html')


def about(request):
    return render(request,'generator/about.html')


def password(request):
    thepassword = 'testing'
    characters = list('abcdefghijklmnopqrstuvwqyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWQYZ'))
    if request.GET.get('symbols'):
        characters.extend(list('!@#$%^&*'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    length = int(request.GET.get('length'))
    thepassword=''
    for x in range(length):
        thepassword += random.choice(characters)
    return render(request,'generator/password.html', {'password':thepassword})

