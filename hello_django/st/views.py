from django.shortcuts import render
from django.http import HttpResponse
from st.models import Person

name = Person.objects.get(first_name='Vova')

def test_funk(requests):
    print(name)
    #print(name)
    print(name.first_name)
    return HttpResponse('Hello world ' + name.first_name)
