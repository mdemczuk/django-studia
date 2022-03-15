import random

from django.shortcuts import render

# Create your views here.

def home_view(request):
    number = random.randint(6, 14)
    context = {
       'some_bool': True,
       'mynumber': number,
       'some_dict': {
        'A': 1,
        'B': 2,
        'C': 3
       },
       'some_lst': [
          random.randint(1, 10),
          random.randint(1, 10),
          random.randint(1, 10),
       ]
    }

    return render(request, 'myapp/index.html', context)


def contact_view(request):
    return render(request, 'myapp/contact.html')