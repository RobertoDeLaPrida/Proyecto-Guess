from django.shortcuts import render
import random


# Create your views here.

def home(request):
    return render(request, 'adivina/home.html')


def guess(request):
    numero =random.randint(1,100)
    num_usr=int(request.POST('numerito'))

    if num_usr == numero:
        mensaje='Felicidades!!!! Has adivinado el numero'
    elif num_usr > numero:
        mensaje='Vaya, has fallado. El numero que has introducido es mayor que el numero a adivinar'
    elif num_usr < numero:
        mensaje='Vaya, has fallado. El numero que has introducido es menor que el numero a adivinar'
    
    return render(request, 'adivina/guess.html', {'mensaje': mensaje})