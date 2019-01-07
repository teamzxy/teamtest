from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import CelebSerializer,categorySerializer
from .models import crawl,box
from .category_list import racingmodel_list, announcer_list
#-------------------------#
from background_task import background
from django.utils import timezone

class crawlViewSet(viewsets.ModelViewSet):

    queryset = crawl.objects.all()
    serializer_class = CelebSerializer

    def create(self,request,pk=None):
        cnt=1
        mymodel = request.data['post_category']
        slist(mymodel,schedule=timezone.now())
        return Response("ok")

@background(schedule=60)
def slist(request):
    names=[]
    cnt=1
    if request == "레이싱 모델":
        link = racingmodel_list(request)
        for area in link:
            for v in area.find_all("div","wiki-heading-content"):
                for b in v.find_all("li")[2:]:
                    names.append(b.text.split('[')[0])

    elif request == "기자":
        link = announcer_list(request)
        for person_index in link:
            if '황선필' in names:
                break
            for k in person_index.find_all("a",{"class":"wiki-link-internal"}):
                k=k.text.split()[0]
                if len(k)<4:
                    names.append(k)

    print(">>>>",names)

    for t in names:
        box(mylist=t,id=cnt).save()
        cnt+=1
