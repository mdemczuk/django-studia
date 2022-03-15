import requests
from django.shortcuts import render

SOURCES = [
    {'id': 'new-scientist', 'name': 'The New Scientist'},
    {'id': 'techradar', 'name': 'TechRadar'},
    {'id': 'national-geographic', 'name': 'National Geographic'},
    {'id': 'ars-technica', 'name': 'Ars Technica'},
    {'id': 'mashable', 'name': 'Mashable'},
]

def index_view(request, source='new-scientist'):
    API_KEY = '25ec709ac0724787a51dff4a71332ab2'

    url = ('https://newsapi.org/v2/everything?'
        f'sources={source}&'
        f'apiKey={API_KEY}')

    response = requests.get(url)
    data = response.json()

    context = {
        'newsapi': data,
        'sources': SOURCES, 
        'active_source': source
    }
    print(data['articles'][0]['author'])

    return render(request, 'news/index.html', context)