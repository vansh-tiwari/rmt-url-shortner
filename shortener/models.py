from .util import *
from django.db import models

# Create your models here.
class RmtURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(RmtURLManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=False)
        return qs
    
    def refresh_codes(self, items=None):
        qs = RmtURL.objects.filter(id__gte=1)
        if items is not None and isinstance(items, int):
            qs = qs.order_by('-id')[:items]

        newcodes = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            print(q.shortcode)
            q.save()
            newcodes+=1

        return "New codes made: {i}".format(i=newcodes)

class RmtURL(models.Model):
    url = models.CharField(max_length=220,)
    shortcode = models.CharField(max_length = 15, unique=True, blank=True )
    updated = models.DateTimeField(auto_now = True)
    timestamp = models.DateTimeField(auto_now_add = True)
    active = models.BooleanField(default=True)

    objects = RmtURLManager()
    some_random = RmtURLManager()


    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        super(RmtURL, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)