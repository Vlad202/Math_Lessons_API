from rest_framework import generics
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from adminPanel.serializers import UsersListSetSerializer, BanUserSerializer, CreateThemeSerializer, ThemeListSerializer, CreateTopicSerializer, CreateTestSerializer
from adminPanel.models import BanUserModel, GlobalThemeModel, SubtopicModel, TestModel
from authApp.models import UserAgent, UserToken
from adminPanel.permisions import is_staff_only

class ThemeListView(APIView):
    serializer = ThemeListSerializer
    def get(self, request):
        if is_staff_only(request.COOKIES["Cookie"]):
            themes = GlobalThemeModel.objects.all()
            themes_queryset = []
            for theme in themes:
                themes_queryset.append([theme.id, theme.header])
            return Response({'users': themes_queryset})
        else:
            return Response({'error': 'invalid token'})

class UsersListView(APIView):
    serializer = UsersListSetSerializer
    def get(self, request):
        if is_staff_only(request.COOKIES["Cookie"]):
            users = User.objects.all()
            users_queryset = []
            for user in users:
                user_info = [user.username, user.email]
                users_queryset.append(user_info)
            return Response({'users': users_queryset})
        else:
            return Response({'error': 'invalid token'})

class GiveBanView(APIView):
    serializer = BanUserSerializer
    def post(self, request):
        if is_staff_only(request.COOKIES["Cookie"]):
            try:
                bad_user_email = UserAgent.objects.get(email=request.POST['email'])
            except:
                return Response({'error': 'invalid email'})
            if BanUserModel.objects.filter(email=bad_user_email.email).exists():
                return Response({'error': 'user is alredy banned'})
            else:
                banned_user = BanUserModel.objects.create(
                    ip_agent = bad_user_email.ipAgent,
                    email = bad_user_email.email,
                )
                banned_user.save()
                User.objects.get(email=request.POST['email']).delete()
                return Response({'user': 'is banned'})
        else:
            return Response({'error': 'invalid token'})

class Createtheme(APIView):
    serializer = CreateThemeSerializer
    def post(self, request):
        if is_staff_only(request.COOKIES["Cookie"]):
            theme = GlobalThemeModel.objects.create(
                header = request.POST["header"]
            )
            theme.save()
            return Response({'success': 'global theme created'})
        else:
            return Response({'error': 'invalid token'})

class EditThemeView(APIView):
    serializer = CreateThemeSerializer
    def post(self, request, theme):
        if is_staff_only(request.COOKIES["Cookie"]):
            try:
                global_theme = GlobalThemeModel.objects.get(header=theme)
            except:
                return Response({'error': 'unknown theme'})
            global_theme.header = request.POST["header"]
            global_theme.save()
            return Response({'success': 'theme has been edited'})
        else:
            return Response({'error': 'invalid token'})    

class EditSubtopicView(APIView):
    serializer = CreateTopicSerializer
    def post(self, request, subtopic):
        if is_staff_only(request.COOKIES["Cookie"]):
            try:
                subtopic = SubtopicModel.objects.get(header=subtopic)
            except:
                return Response({'error': 'unknown subtopic'})
            subtopic.header = request.POST["header"]
            subtopic.body_article = request.POST["body"]
            subtopic.save()
            return Response({'success': 'topic has been edited'})
        else:
            return Response({'error': 'invalid token'})  

class EditTestView(APIView):
    serializer = CreateTestSerializer
    def post(seld, request, id):
        if is_staff_only(request.COOKIES["Cookie"]):
            try:
                test = TestModel.objects.get(id=id)
            except:
                return Response({'error': 'unknown subtopic or test'})
            test.question = request.POST["question"]
            test.answer = request.POST["answer"]
            test.save()
            return Response({'success': 'test has been edited'})
        else:
            return Response({'error': 'invalid token'})  

class CreatetopicView(APIView):
    serializer = CreateTopicSerializer
    def get(seld, request, theme):
        if is_staff_only(request.COOKIES["Cookie"]):
            try:
                global_theme = GlobalThemeModel.objects.get(header=theme)
            except:
                return Response({'error': 'unknown theme'})
            queryset = SubtopicModel.objects.filter(global_theme=global_theme)
            topics_themes = []
            for item in queryset:
                topics_themes.append([item.id, item.header])
            return Response({"theme": theme, "subtopics": topics_themes})
        else:
            return Response({'error': 'invalid token'})

    def post(seld, request, theme):
        if is_staff_only(request.COOKIES["Cookie"]):
            try:
                global_theme = GlobalThemeModel.objects.get(header=theme)
            except:
                return Response({'error': 'unknown theme'})
            subtopic = SubtopicModel.objects.create(
                global_theme = global_theme,
                header = request.POST["header"],
                body_article = request.POST["body"]
            )
            subtopic.save()
            return Response({'success': 'true'})
        else:
            return Response({'error': 'invalid token'})

class TestView(APIView):
    serializer = CreateTestSerializer
    def get(self, request, subtopic):
        if is_staff_only(request.COOKIES["Cookie"]):
            try:
                subtopic = SubtopicModel.objects.get(header=subtopic)
            except:
                return Response({'error': 'unknown subtopic'})
            tests = TestModel.objects.filter(topic=subtopic)
            test = []
            for item in tests:
                test.append([item.id, item.question, item.answer])
            return Response({'questions': test})
        else:
            return Response({'error': 'invalid token'})
    
    def post(self, request, subtopic):
        if is_staff_only(request.COOKIES["Cookie"]):
            try:
                subtopic_model = SubtopicModel.objects.get(header=subtopic)
            except:
                return Response({'error': 'unknown subtopic'})
            test = TestModel.objects.create(
                question = request.POST["question"],
                answer = request.POST["answer"],
                topic = subtopic_model
            )
            test.save()
            return Response({'success': 'true'})
        else:
            return Response({'error': 'invalid token'})