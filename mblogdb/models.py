from django.db import models
from django.contrib.auth.models import User

class UserDetail(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    nickname = models.CharField(max_length=30)
    self_describe = models.TextField(blank=True)
    mail = models.EmailField(blank=True, unique=True)
    image = models.URLField(blank=True)
    birthday = models.DateField(blank=True, null=True)
    city = models.IntegerField(blank=True, null=True)
    sex = models.NullBooleanField(blank=True)
    sexual_orientation = models.IntegerField()

    def __unicode__(self):
        return self.nickname

