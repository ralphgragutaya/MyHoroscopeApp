from django.shortcuts import render

from .forms import HoroscopeForm

import requests
import json

def get_horoscope(request):
    horoscope = ''
    if request.method == 'POST':
        form = HoroscopeForm(request.POST)
        if form.is_valid():
            zodiac_sign = form.cleaned_data['zodiac_sign']
            period = form.cleaned_data['period']

            horoscope_retriever = HoroscopeRetriever(zodiac_sign)
            horoscope_response = horoscope_retriever.get_horoscope_by_period(
                period)
            if horoscope_response.status_code == 200: # 200 means okay in web (standard)
                horoscope = json.loads(horoscope_response.text)['horoscope'][2:]
    else:
        form = HoroscopeForm()
    return render(request, 'home.html', {'form': form, 'horoscope': horoscope})

class HoroscopeRetriever:

    def __init__(self, zodiac_sign):
        self.base_url = 'http://horoscope-api.herokuapp.com/horoscope'
        self.zodiac_sign = zodiac_sign

    def get_horoscope_by_period(self, period):
        return requests.get('{url}/{period}/{zodiac_sign}'.format(
            url = self.base_url,
            period = period,
            zodiac_sign = self.zodiac_sign
        ))
