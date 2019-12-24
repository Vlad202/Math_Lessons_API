from django.contrib import admin
from adminPanel.models import BanUserModel, GlobalThemeModel, SubtopicModel, TestModel

admin.site.register(BanUserModel)
admin.site.register(GlobalThemeModel)
admin.site.register(SubtopicModel)
admin.site.register(TestModel)