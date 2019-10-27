import random
import string
from django.db import models

# Create your models here.
def code_generator(size = 6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

class RmtURL(models.Model):
    url = models.CharField(max_length=220,)
    shortcode = models.CharField(max_length = 15, unique=True )
    updated = models.DateTimeField(auto_now = True)
    timestamp = models.DateTimeField(auto_now_add = True)

    def save(self, *args, **kwargs):
        self.shortcode = code_generator()
        super(RmtURL, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)