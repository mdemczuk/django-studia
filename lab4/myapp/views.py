import random
import re
import urllib.request

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

def about_view(request):
   number1 = random.randint(1, 10)
   number2 = random.randint(1, 10)
   context = {
      'lucky_number': number1,
      'unlucky_number': number2,
      'mytech': [
         {
            'name': 'HTML',
            'url': 'https://www.w3schools.com/html/',
            'level': 'beginner'
         },
         {
            'name': 'CSS',
            'url': 'https://www.w3schools.com/css/',
            'level': 'beginner'
         },
         {
            'name': 'Bootstrap',
            'url': 'https://getbootstrap.com',
            'level': 'beginner'
         },
         {
            'name': 'Python',
            'url': 'https://www.python.org',
            'level': 'intermediate'
         },
         {
            'name': 'Django',
            'url': 'https://www.djangoproject.com',
            'level': 'beginner'      
         },    
      ]
   }
   return render(request, 'myapp/about.html', context)

def genbank_view(request):
   with urllib.request.urlopen('ftp://ftp.ncbi.nlm.nih.gov/genbank/README.genbank') as response:
      html = response.read()

   decoded_html = html.decode('utf-8')
   release_ver = re.findall("GenBank Flat File Release\\s+(.+)\\s+", decoded_html)[0]
   release_date = re.findall("Release Date:\\s+(.+)\\s+", decoded_html)[0]

   context = {
      'version': release_ver,
      'date': release_date
   }

   return render(request, 'myapp/genbank.html', context)