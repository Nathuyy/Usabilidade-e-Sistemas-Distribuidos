from django.db import models

# Create your models here.
class Person(models.Model):
    firs_name = models.CharField('first_Name', max_length=50)
    last_name = models.CharField('last_name', max_length=100)
    address =  models.CharField('address', max_length=100)
    phone =  models.CharField('phone', max_length=100)
    email = models.EmailField('email')

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'Persons'
        ordering =['id']

    def __str__(self):
        return f'{self.id} - {self.firs_name}'