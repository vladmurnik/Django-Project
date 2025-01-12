from django.shortcuts import render
from .models import Prime_numbers
import asyncio
import time
from PIL import Image
def prime(n,simples):
    a = 1
    i = 1
    while len(simples) != n:
        b = 0
        a += 1
        for i in range(len(simples)):
            if a % simples[i] == 0:
                b += 1
        if b == 0:
            simples.append(a)
            print(a)
            Prime_numbers.objects.create(numbers=a)
            i += 1
def number(request):
    list = []
    i = 0
    for i in range(Prime_numbers.objects.count()):
        i += 1
        list.append(Prime_numbers.objects.get(id = i).numbers)
    prime(1+len(list),list)
    return render(request,"prime_number/index.html",{"numbers":(str(list))[1:-1]})
