from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from adminPanel.models import SubtopicModel, GlobalThemeModel
from adminPanel.permisions import user_is_auth
from django.core import serializers
from study.serializers import SubtopicSerializer
from django.core import serializers
import json

class LessonsView(APIView):
    def get(self, request):
        token = request.COOKIES["Token"]
        if user_is_auth(token):
            serializer = json.loads(serializers.serialize('json', SubtopicModel.objects.all()))



            # data = {}
            # for i in serializer:
            #     if i["fields"]["global_theme"] not in data:
            #         data[i["fields"]["global_theme"]] = list(i["fields"]["header"])
            #     else:
            #         data[i["fields"]["global_theme"]].append(i["fields"]["header"])
            data = {}
            for d in serializer:
                d["fields"]["global_theme"] = GlobalThemeModel.objects.get(id=int(d["fields"]["global_theme"])).header
                if d["fields"]["global_theme"] not in data:
                    data[d["fields"]["global_theme"]] = []
                    data[d["fields"]["global_theme"]].append(d["fields"]["header"])
                else:
                    data[d["fields"]["global_theme"]].append(d["fields"]["header"])
            

            return Response(data)
        else:
            return Response({
                'status': 'Bad request',
                'message': 'Account could not be created with received data.'
            }, status=400)