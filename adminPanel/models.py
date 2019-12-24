from django.db import models

class BanUserModel(models.Model):
    ip_agent = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    def __str__(self):
        return self.email

class GlobalThemeModel(models.Model):
    header = models.CharField(max_length=256)
    def __str__(self):
        return self.header

class SubtopicModel(models.Model):
    header = models.CharField(max_length=256)
    body_article = models.TextField(blank=True)
    global_theme = models.ForeignKey(GlobalThemeModel, on_delete=models.CASCADE)
    def __str__(self):
        string = self.header + ' (' + self.global_theme.header + ')'
        return string

class TestModel(models.Model):
    question = models.CharField(max_length=2048)
    answer = models.CharField(max_length=512)
    topic = models.ForeignKey(SubtopicModel, on_delete=models.CASCADE)
    def __str__(self):
        string = self.question + ' (' + self.topic.header + ')'
        return string
