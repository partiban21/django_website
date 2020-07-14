from __future__ import unicode_literals

from django.db import models

#not used
class Profile(models.Model):
    text = models.CharField(max_length=4096)

#user account object and attributes
class Account(models.Model):
    email = models.CharField(max_length=16,primary_key=True)
    password = models.CharField(max_length=16)
    firstName = models.CharField(max_length=16)
    lastName = models.CharField(max_length=16)
    phoneNum = models.CharField(max_length=16)
    profile = models.OneToOneField(Profile, null=True)
    #following = models.ManyToManyField("self", symmetrical=False)

    def __str__(self):
        return self.email

#user article object and attributes
class Article(models.Model):
    header = models.CharField(max_length=4,primary_key=True)
    likes = models.IntegerField(default=0)
    #likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='psot_likes')

    def __str__(self):
        return self.header

#user comment object and attributes,contains forkeign key to which article comment is for
class Comments(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Account, related_name='%(class)s_user')
    article = models.ForeignKey(Article, related_name='%(class)s_header')
    time = models.DateTimeField()
    text = models.CharField(max_length=4096)

#user ArticleAccountLiked object and is table that stores which user have commented on which article
class ArticleAccountLiked(models.Model):
    id = models.AutoField(primary_key=True)
    article = models.ForeignKey(Article, related_name='%(class)s_header')
    user = models.ForeignKey(Account, related_name='%(class)s_user')
