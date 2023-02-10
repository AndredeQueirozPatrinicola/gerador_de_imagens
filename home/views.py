from django.shortcuts import render
from django.http import JsonResponse

import json
import openai
from decouple import config

# Create your views here.


def index(request):
    return render(request, 'index.html')

def submit(request):

    if request.method == 'POST': 
        body = json.loads(request.body.decode('utf-8'))
        content = body.get('content')

        openai.api_key = config('API_KEY')
        request = openai.Image.create(
            prompt=content,
            n=1,
            size="512x512"
        )
        response = request['data'][0]['url']

        return JsonResponse({'url': response})


    
    else:
        print(request.GET)
        # openai.api_key = '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'
        # texto = request.POST.get('texto')
        # response = openai.Image.create(
        #                 prompt=texto,
        #                 n=1,
        #                 size="512x512"
        #                 )
        # image_url = response['data'][0]['url']
        image_url = 'oi'

        return JsonResponse({'url': image_url})
