from django.shortcuts import render
from random import choice
import string


def homepage(requests):
    return render(requests, 'generator/home.html')


def description(requests):
    return render(requests, 'generator/desc.html')


def password(requests):
    length = int(requests.GET.get("length"))
    is_upper = requests.GET.get("uppercase")
    is_num = requests.GET.get("number")
    is_spec = requests.GET.get("special")

    alphabet_lower = string.ascii_lowercase
    alphabet_upper = string.ascii_uppercase
    numbers = string.digits
    special_symbol = '!@#$%^&?'

    the_password = ''
    if is_upper:
        alphabet_lower += alphabet_upper
    if is_num:
        alphabet_lower += numbers
    if is_spec:
        alphabet_lower += special_symbol

    for i in range(length):
        the_password += choice(alphabet_lower)

    return render(requests, 'generator/password.html', {"password": the_password})


