from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import HttpResponse
from .serializers import parsingSerializer
from .models import parsing
from rest_framework import status
import requests
from bs4 import BeautifulSoup

import os

class parsingViewSet(viewsets.ModelViewSet):

    queryset = parsing.objects.all()
    serializer_class = parsingSerializer

    def create(self,request,pk=None):

        cat_name=request.data['post_category']
        if cat_name == "기자":
            url = "https://namu.wiki/w/기자/목록"

            html = requests.get(url).text
            soup = BeautifulSoup(html, 'html.parser')

            person_list = soup.find_all("div",{"class":"wiki-heading-content"})

            names=[]
            for person_index in person_list:
                if '황선필' in names:
                    break
                for k in person_index.find_all("a",{"class":"wiki=link-internel"}):
                    k=k.text.split()[0]
                    if len(k)<4:
                        names.append(k)
            for i in names:
                print(i)

        res = {"cat_name":cat_name,"cat_path":url,"test":names,"html":html}
        return Response(res)
