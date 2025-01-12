from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.http import JsonResponse
import hashlib
from .models import Cipher
import random
import string
from .adik_1 import cipher_adik_text, decipher_adik_text, cipher_adik_text_2, decipher_adik_text_2
def block_1(text):
    return text[::-1]
def block_2(text):
    txt = ''
    for i in range(10):
        txt += random.choice(string.ascii_lowercase)
    return text + txt
def block_3(text):
    str_ASCII = ''
    for i in text:
        str_ASCII += str(ord(i)) + '_'
    return str_ASCII

def block(text,cipher,key):
    for i in key:
        if i == '1':
            text = block_1(text)
        elif i == '2':
            text = block_2(text)
        elif i == '3':
            text = block_3(text)
    return text

def cipher_adik(request):
    result = None
    input_data = None
    key = None
    deresult = None
    deinput_data = None
    dekey = None
    cipher = None
    if request.method == "POST":
        # Получаем данные из формы
        input_data = request.POST.get("input_data")
        cipher = request.POST.get("cipher")
        key = request.POST.get("key")
        dekey = request.POST.get("dekey")
        deinput_data = request.POST.get("deinput_data")
        # Сохраняем в базу данных
        # хуйня
        #try:
        #    i = 0
        #    cipher_text_list = []
        #    while True:
        #        i = i + 1
        #        q = Cipher.objects.get(id=i)
        #        cipher_text_list.append(q.text_cipher)
        #except:
        #    print(set(cipher_text_list))
        if input_data != None and key != None:
            if cipher == "adik_1":
                result = cipher_adik_text(input_data, key)
            elif cipher == 'adik_2':
                result = cipher_adik_text_2(input_data, key)
            else:
                result = block(input_data, cipher, key)
        elif deinput_data != None and dekey != None:
            if cipher == "adik_1":
                deresult = decipher_adik_text(deinput_data, dekey)
            elif cipher == 'adik_2':
                deresult = decipher_adik_text_2(deinput_data, dekey)
            else:
                deresult = block(deinput_data, cipher, dekey)


    return render(request, "haha/adik.html", {"result": result,
                                              "input_data": input_data,
                                              "cipher": cipher,
                                              "key": key,
                                              "deresult": deresult,
                                              "deinput_data": deinput_data,
                                              "dekey": dekey,
    })
def cipher_text(text,cipher):
    # Шифруем текст
    hash_function = getattr(hashlib,cipher)
    hash_object = hash_function()
    text = bytes(text, encoding='utf-8')
    hash_object.update(text)
    return (hash_object.hexdigest())

def cipher(request):
    result = None  # Переменная для результата
    input_data = None
    cipher = None
    if request.method == "POST":
        # Получаем данные из формы
        input_data = request.POST.get("input_data")
        cipher = request.POST.get("cipher")

        # Сохраняем в базу данных
        Cipher.objects.create(text_cipher = input_data)
        # хуйня
        try:
            i = 0
            cipher_text_list = []
            while True:
                i = i + 1
                q = Cipher.objects.get(id=i)
                cipher_text_list.append(q.text_cipher)
        except:
            print(set(cipher_text_list))

        # Обрабатываем данные
        result = cipher_text(input_data,cipher)

    # Рендерим шаблон с результатом
    return render(request, "haha/index.html", {"result": result,"input_data": input_data, "cipher": cipher})

def decipher(request):
    result = None  # Переменная для результата
    input_data = None
    cipher = None
    if request.method == "POST":
        # Получаем данные из формы
        input_data = request.POST.get("input_data")
        cipher = request.POST.get("cipher")

        # Сохраняем в базу данных
        Cipher.objects.create(text_cipher = input_data)
        # хуйня
        try:
            i = 0
            cipher_text_list = []
            while True:
                i = i + 1
                q = Cipher.objects.get(id=i)
                cipher_text_list.append(q.text_cipher)
        except:
            print(set(cipher_text_list))

        # Обрабатываем данные
        result = cipher_text(input_data,cipher)

    # Рендерим шаблон с результатом
    return render(request, "haha/index.html", {"result": result,"input_data": input_data, "cipher": cipher})