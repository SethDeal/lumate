from django.db import models
from django.core.urlresolvers import reverse

class Post(models.Model):
    firstName = models.CharField(max_length=100)
    lastName  = models.CharField(max_length=100)
    address = models.CharField(max_length = 50)
    content = mosels.TextField()
    date = models.DateTimeField(auto_now_add=True)

    slug = models.SlugField(unique=True,max_length = 255)

    class Meta:
	ordering = ['-created']
    def __unicode__(self):
	return u'%s'%self.title

    def get_absolute_url(self):
	return reverse('guestbook.views.post',args=[self.slug])

# Create your models here.
