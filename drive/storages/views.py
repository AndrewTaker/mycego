from django.shortcuts import render
import requests
from dotenv import load_dotenv
from os import getenv

load_dotenv()
# b1321b86d3c0471e21a23d4f58e9352c037e6c7d54e103f77b2fe2106be52cfa

def index(request):
    url = "https://cloud-api.yandex.net/v1/disk/resources/files"
    params = {
        "limit": 3,

    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"OAuth {getenv('YA_TOKEN')}",
    }
    
    response = requests.get(url, params=params, headers=headers)
    
    return render(request, "storages/index.html", response.json())
