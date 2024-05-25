import requests

def get_products():
    response = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(response.json())
