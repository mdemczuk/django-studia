import requests
from django.shortcuts import render

COUNTRIES = [
    {'country_code': 'PL', 'name': 'Poland'},
    {'country_code': 'DE', 'name': 'Germany'},
    {'country_code': 'AT', 'name': 'Austria'},
    {'country_code': 'BE', 'name': 'Belgium'},
    {'country_code': 'IT', 'name': 'Italy'},
    {'country_code': 'CN', 'name': 'China'},
    {'country_code': 'US', 'name': 'United States'},
]

def index_view(request, source='PL'):

    url = (f'https://api.covid19api.com/summary')

    response = requests.get(url)
    data = response.json()


    context = {
        'global_data': data['Global'],
        'countries': COUNTRIES,
        'current_country_code': source,
    }


    for country in data['Countries']:
        if country['CountryCode'] == source:
            context['selected_country'] = country
            break

    return render(request, 'covid19/index.html', context)