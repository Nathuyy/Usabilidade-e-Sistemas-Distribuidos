from django.db import models

# Create your models here.
class Socialnetwork(models.Model):
    name = models.CharField('name', max_length=50)
    content_type = models.TextField('content_type', max_length=100)
    url =  models.URLField('url', max_length=100)

    class Meta:
        verbose_name = 'Socialnetwork'
        verbose_name_plural = 'Socialnetwork'
        ordering =['id']

    def __str__(self):
        return f'{self.id} - {self.name} - {self.content_type} - {self.url}'