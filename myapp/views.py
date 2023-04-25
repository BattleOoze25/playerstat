from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . models import Player, Score
from . serializers import PlayerSerializer
from . cron import get_sheet_data
@api_view(['GET'])
def get_player_average(request):
    get_sheet_data()
    objs = Player.objects.all()
    # objs = PlayerSerializer(objs, many=True)
    
    lst = []
    for i in objs:
        scores = Score.objects.filter(player = i)
        sum_ =0
        avg=0
        print("\n")
        if len(scores) >=5:
            for j in range(-(len(scores)-1), -(len(scores)-6)):
                print(scores[-j].score, " ")
                sum_ += scores[-j].score
                avg = sum_/5
        else:
            print("hello")
            for j in range(0, len(scores)):
                print(scores[j].score, " ")
                sum_ += scores[j].score
                avg = sum_/len(scores)


        lst.append({
            'name':i.name,
            'average':avg
        })


    
    return Response({"message":"hello", "data":lst})