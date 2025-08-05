# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    department = models.CharField(max_length=255, null=True, blank=True)
    last activity = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Crawler Config(models.Model):

    #__Crawler Config_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)
    is active = models.BooleanField()
    portal = models.ForeignKey(Portal, on_delete=models.CASCADE)
    selector = models.ForeignKey(Selector, on_delete=models.CASCADE)

    #__Crawler Config_FIELDS__END

    class Meta:
        verbose_name        = _("Crawler Config")
        verbose_name_plural = _("Crawler Config")


class Portal(models.Model):

    #__Portal_FIELDS__
    domain = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    origin = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)

    #__Portal_FIELDS__END

    class Meta:
        verbose_name        = _("Portal")
        verbose_name_plural = _("Portal")


class Selector(models.Model):

    #__Selector_FIELDS__
    query = models.CharField(max_length=255, null=True, blank=True)
    method = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=255, null=True, blank=True)

    #__Selector_FIELDS__END

    class Meta:
        verbose_name        = _("Selector")
        verbose_name_plural = _("Selector")


class Scraper Config(models.Model):

    #__Scraper Config_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    is active = models.BooleanField()
    portal = models.ForeignKey(Portal, on_delete=models.CASCADE)
    selector = models.ForeignKey(Selector, on_delete=models.CASCADE)

    #__Scraper Config_FIELDS__END

    class Meta:
        verbose_name        = _("Scraper Config")
        verbose_name_plural = _("Scraper Config")


class Raw Url(models.Model):

    #__Raw Url_FIELDS__
    url = models.TextField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    domain = models.ForeignKey(Portal, on_delete=models.CASCADE)

    #__Raw Url_FIELDS__END

    class Meta:
        verbose_name        = _("Raw Url")
        verbose_name_plural = _("Raw Url")


class Clean Url(models.Model):

    #__Clean Url_FIELDS__
    url = models.TextField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    domain = models.ForeignKey(Portal, on_delete=models.CASCADE)
    raw url = models.ForeignKey(Raw Url, on_delete=models.CASCADE)

    #__Clean Url_FIELDS__END

    class Meta:
        verbose_name        = _("Clean Url")
        verbose_name_plural = _("Clean Url")


class Content(models.Model):

    #__Content_FIELDS__
    title = models.CharField(max_length=255, null=True, blank=True)
    body = models.TextField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    images = models.CharField(max_length=255, null=True, blank=True)
    authors = models.TextField(max_length=255, null=True, blank=True)
    published at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    language = models.CharField(max_length=255, null=True, blank=True)
    clean url = models.ForeignKey(Clean Url, on_delete=models.CASCADE)
    domain = models.ForeignKey(Portal, on_delete=models.CASCADE)

    #__Content_FIELDS__END

    class Meta:
        verbose_name        = _("Content")
        verbose_name_plural = _("Content")


class Transaction(models.Model):

    #__Transaction_FIELDS__
    id = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    metadata = models.CharField(max_length=255, null=True, blank=True)
    crawler config = models.ForeignKey(Crawler Config, on_delete=models.CASCADE)
    scraper config = models.ForeignKey(Scraper Config, on_delete=models.CASCADE)
    raw url = models.ForeignKey(Raw Url, on_delete=models.CASCADE)
    clean url = models.ForeignKey(Clean Url, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    servers = models.ForeignKey(Scrapyd Servers, on_delete=models.CASCADE)

    #__Transaction_FIELDS__END

    class Meta:
        verbose_name        = _("Transaction")
        verbose_name_plural = _("Transaction")


class Activity(models.Model):

    #__Activity_FIELDS__
    user = models.CharField(max_length=255, null=True, blank=True)
    action = models.CharField(max_length=255, null=True, blank=True)
    ip_address = models.CharField(max_length=255, null=True, blank=True)
    user_agent = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    timestamp = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Activity_FIELDS__END

    class Meta:
        verbose_name        = _("Activity")
        verbose_name_plural = _("Activity")


class Scrapyd Servers(models.Model):

    #__Scrapyd Servers_FIELDS__
    user = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    port = models.CharField(max_length=255, null=True, blank=True)

    #__Scrapyd Servers_FIELDS__END

    class Meta:
        verbose_name        = _("Scrapyd Servers")
        verbose_name_plural = _("Scrapyd Servers")


class Statistics(models.Model):

    #__Statistics_FIELDS__
    type = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    run count = models.IntegerField(null=True, blank=True)
    success count = models.IntegerField(null=True, blank=True)
    failure count = models.IntegerField(null=True, blank=True)
    avg response time = models.IntegerField(null=True, blank=True)
    crawler config = models.ForeignKey(Crawler Config, on_delete=models.CASCADE)
    scraper config = models.ForeignKey(Scraper Config, on_delete=models.CASCADE)

    #__Statistics_FIELDS__END

    class Meta:
        verbose_name        = _("Statistics")
        verbose_name_plural = _("Statistics")



#__MODELS__END
