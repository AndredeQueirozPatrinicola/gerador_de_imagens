from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response

from home import serializers

import json
import openai
from decouple import config

# Create your views here.


def index(request):
    return render(request, 'index.html')


class ImageGeneratorAPI(APIView):

    def post(self, request, *args, **kwargs):
        openai.api_key = config('API_KEY')
        try:
            body = json.loads(request.body.decode('utf-8'))
            content = body.get('content')
            request = openai.Image.create(
                                            prompt=content,
                                            n=1,
                                            size="512x512"
                                        )
            response = {
                'url' : request['data'][0]['url']
            }
            serializer = serializers.ImageSerializer(response)
        except:
            response = {
                'status_code' : 406,
                'detail' : "Request denied by OpenAi API. Some expressions are not allowed. Verify if your text have political content, drugs, violence or sexual content"
            }
            serializer = serializers.ErroSerializer(response)
        finally:
            return Response(serializer.data)