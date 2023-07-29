from django.shortcuts import render

def exchange(request):
     name = 'Santa Claus'

     context = {
          'name': name
     }
     return render(request=request, 
                   template_name='currency_exchange/index.html', 
                   context=context)

