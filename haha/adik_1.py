import random
import string


def cipher_adik_text(text,key):
    key_str = ''
    while len(key_str) < len(text):
        for i in key:
            key_str += i
    ASCII_num_list = []
    for i in text:
        ASCII_num_list.append(ord(i))
    print(ASCII_num_list)
    num_list = []
    for num, i in enumerate(ASCII_num_list):
        num_list.append(i+ord(key_str[num]))
    print(num_list)
    result = ''
    for i in num_list:
        result+= str(i) + random.choice(string.ascii_lowercase)
    return result

def decipher_adik_text(text,key):
    key_str = ''
    while len(key_str) < len(text):
        for i in key:
            key_str += i

    list_norandom = [i for i in text]
    list_norandom_int = []
    for i in list_norandom:
        try:
            if not (isinstance(int(i), str)):
                list_norandom_int.append(i)
        except ValueError:
            pass
    list_int = []
    stri = ''
    dl = 0
    for i in text:
        try:
            if not (isinstance(int(i), str)):
                dl += 1
        except ValueError:
            break
    for i in list_norandom_int:
        stri += i
        if len(stri) == dl:
            list_int.append(int(stri))
            stri = ''
    print(list_int)
    num_list = []
    for num, i in enumerate(list_int):
        num_list.append(i - ord(key_str[num]))
    print(num_list)
    result = ''
    for i in num_list:
        result += chr(i)
    return result

def cipher_adik_text_2(text,key):
    result = ''
    mas_text = [i for i in text]
    while len(key) < len(text):
        key += key
    for num, i in enumerate(mas_text):
        result += str(ord(i)*ord(key[num])) + random.choice(string.ascii_lowercase)
    return result
def decipher_adik_text_2(text,key):
    result = ''
    text_mas_sl = []
    while len(key) < len(text):
        key += key
    z = ''
    for i in text:
        if not(i.isdigit()):
            text_mas_sl.append(z)
            z = ''
        else:
            z += i
    text_mas_sl_2 = []
    for i in text_mas_sl:
        if i != '':
            text_mas_sl_2.append(i)
    text_mas_sl_3 = []
    for num, i in enumerate(text_mas_sl_2):
        text_mas_sl_3.append(chr(round((int(i))/ord(key[num]))))
    for i in text_mas_sl_3:
        result += i
    return result