from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    city = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.first_name if self.first_name else self.username


# NAMAZ MODEL


NAMAZ_TYPES = (('Fajar', 'Fajar'), ('Zuhar', 'Zuhar'), ('Asar', 'Asar'),
               ('Maghrib', 'Maghrib'), ('Isha', 'Isha'), ('Tahajjud', 'Tahajjud'))


DONE_TYPES = (('Jamat', 'Jamat'), ('Individual', 'Individual'),
              ('Kaza', 'Kaza'), ('Not Prayed', 'Not Prayed'))


class Salah(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    type = models.CharField(max_length=10, choices=NAMAZ_TYPES)
    done = models.CharField(max_length=20, choices=DONE_TYPES)
    date = models.DateField()

    def __str__(self):
        return "{} - {} - {} - {}".format(self.user, self.date, self.type, self.done)

    class Meta:
        verbose_name_plural = 'Salah'
        unique_together = ('user', 'type', 'date')


class Tilawat_e_Quran(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)


class Fast(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    date = models.DateField()


class Donation(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    date = models.DateField()

