# django-currency-converter
A simple currency converter made with Django

How to deploy:
1. Create virtual environment (Terminal)
  \npython3 -m venv venv
2. Activate virtual environment (Terminal)

  source venv/bin/activate
3. Install necessary libraries (Django and Requests)

  pip install django requests
4. Create Django project (name=app)

  django-admin startproject app
5. In the root directory app/ create application (name=currency_exchange)

  django-admin startapp currency_exchange
6. Add created application into 'INSTALLED_APPS' in app/currency_exchange/settings.py
