#coding=utf-8
from django.db import models
from django.contrib.auth.models import User

class UserDetail(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    nickname = models.CharField(max_length=30, unique=True)
    self_describe = models.TextField(blank=True)
    mail = models.EmailField(unique=True)
    image = models.URLField(blank=True)
    birthday = models.DateField(blank=True, null=True)
    city = models.IntegerField(blank=True, null=True)
    sex = models.NullBooleanField(blank=True)
    sexual_orientation = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return unicode(self.nickname)

    def check_follow(self, target_user):
        if Follow.objects.filter(user=self.user,
                                 follow=target_user).count():
            return True
        else:
            return False


class Follow(models.Model):
    user = models.ForeignKey(User, related_name="following")
    # u = User()
    # u.following.count() -> the number of people that u is following
    # u.following.get().follow -> one user that u is following
    # u.following.get().user -> u

    follow = models.ForeignKey(User, related_name="follower")
    # u = User()
    # u.follower.count() -> the number of people who is following u
    # u.follower.get().user -> one user who is following u
    # u.follower.get().follow -> u

    date = models.DateTimeField()

    def __unicode__(self):
        return unicode(self.user)

class Topic(models.Model):
    name = models.CharField(max_length=140)

    def __unicode__(self):
        return unicode(self.name)

class Post(models.Model):
    user = models.ForeignKey(User, related_name="post")
    repo = models.ForeignKey('self', related_name="repoed",
                             blank=True, null=True)
    body = models.TextField()
    encoded_body = models.TextField()
    image = models.TextField(blank=True)
    audio = models.TextField(blank=True)
    video = models.TextField(blank=True)
    topic = models.ManyToManyField(Topic, related_name="post", blank=True)
    like = models.ManyToManyField(User, related_name="like_post", blank=True)
    collect = models.ManyToManyField(User, related_name="collect_post", blank=True)
    date = models.DateTimeField()
    is_active = models.BooleanField()

    def __unicode__(self):
        return unicode(self.id)

    class Meta:
        ordering = ['-date']

    def get_image(self):
        return self.image.split('/////')[1:]

    def get_video(self):
        return self.video.split('/////')[1:]

    def get_audio(self):
        return self.audio.split('/////')[1:]

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comment")
    reco = models.ForeignKey('self', related_name="recoed",
                             blank=True, null=True)
    user = models.ForeignKey(User, related_name="comment")
    body = models.TextField()
    encoded_body = models.TextField()
    like = models.ManyToManyField(User, related_name="like_comment", blank=True)
    collect = models.ManyToManyField(User, related_name="collect_comment", blank=True)
    date = models.DateTimeField()
    is_active = models.BooleanField()

    def __unicode__(self):
        return unicode(self.id)

    class Meta:
        ordering = ['-date']

class Message(models.Model):
    sender = models.ForeignKey(User, related_name="message_send")
    # u = User()
    # u.message_send.count() -> the number of messages that u has sent
    # u.message_send.get() -> one message that u has sent

    recipient = models.ForeignKey(User, related_name="message_received")
    body = models.TextField()
    date = models.DateTimeField()
    is_active = models.BooleanField()

    def __unicode__(self):
        return unicode(self.recipient)

class InformPool(models.Model):
    "new @/Message : send to InformPool; read information: clean InformPool"
    user = models.ForeignKey(User, related_name="information")

    inform_type = models.IntegerField()
    # 0:post
    # 1:comment
    # 2:repo
    # 3:Message

    body = models.TextField()
    date = models.DateTimeField()

    def __unicode__(self):
        return unicode(self.user)

    def get_target(self):
        if self.inform_type == 0 or self.inform_type == 2:
            target = Post.objects.get(id=self.body)
        elif self.inform_type == 1:
            target = Comment.objects.get(id=self.body)
        return target

    def get_type(self):
        if self.inform_type == 0 or self.inform_type == 2:
            return u'微薄'
        elif self.inform_type == 1:
            return u'评论'
