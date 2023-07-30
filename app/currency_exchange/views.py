from django.shortcuts import render
import requests

def exchange(request):
     response = requests.get(url='https://v6.exchangerate-api.com/v6/d42c804b648563db66c26634/latest/USD').json()
     currencies = response.get('conversion_rates')

     if request.method == 'GET':
          context = {
               'currencies': currencies
          }

     return render(request=request, 
                   template_name='currency_exchange/index.html', 
                   context=context)

