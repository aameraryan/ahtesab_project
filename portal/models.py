from django.db import models
from django.contrib.auth.models import AbstractUser
from django.http import Http404
from django.db.models import Q, F
from django.core.exceptions import ObjectDoesNotExist
import datetime
from django.conf import settings
from django.db.models.signals import post_init, post_save


class User(AbstractUser):
    city = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.first_name if self.first_name else self.username


SALAH_PRAY_TYPES = (('Jamat', 'Jamat'), ('Individual', 'Individual'),
              ('Kaza', 'Kaza'), ('Not Prayed', 'Not Prayed'))


class MyDay(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    day_date = models.DateField()
    tahajjud = models.CharField(max_length=20, choices=(('Prayed', 'Prayed'), ('Not Prayed', 'Not Prayed')))
    fajar = models.CharField(max_length=20, choices=SALAH_PRAY_TYPES)
    zuhar = models.CharField(max_length=20, choices=SALAH_PRAY_TYPES)
    asar = models.CharField(max_length=20, choices=SALAH_PRAY_TYPES)
    maghrib = models.CharField(max_length=20, choices=SALAH_PRAY_TYPES)
    isha = models.CharField(max_length=20, choices=SALAH_PRAY_TYPES)
    tilawat = models.BooleanField(default=False)
    zikr = models.BooleanField(default=False)

    def __str__(self):
        return "{} - {}".format(self.user, self.day_date)

    class Meta:
        unique_together = ('user', 'day_date')


# Weakly Records

class MyWeek(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    week_date = models.DateField()
    dawat_muslim = models.BooleanField(default=False)
    dawat_non_muslim = models.BooleanField(default=False)
    hifz = models.BooleanField(default=False)
    usra = models.BooleanField(default=False)
    halq_quran = models.BooleanField(default=False)

    def __str__(self):
        # return "{} - {}".format(self.week_date, self.take_week_name)
        return "{} - {}".format(self.week_date, self.take_year_week_number)

    @property
    def take_month_name(self):
        return self.week_date.strftime('%B %Y')

    @property
    def take_week_name(self):
        return "Weak {} of {}".format(self.take_month_week_number, self.take_month_name)

    @property
    def take_month_week_number(self):
        return (self.week_date.day//8)+1

    @property
    def take_year_week_number(self):
        return self.week_date.isocalendar()
    #
    # def save(self, *args, **kwargs):
    #     all_weaks = self.user.myweek_set.filter(date__month=self.date.month, date__year=self.date.year)
    #     if all_weaks.exists():
    #         for weak in all_weaks:
    #             if weak.take_week_name == self.take_week_name:
    #                 raise Http404
    #         super().save(*args, **kwargs)
    #     else:
    #         super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Week'
        verbose_name_plural = 'Weeks'
        unique_together = ('user', 'week_date')


# def validate_unique_week(sender, instance, *args, **kwargs):
#     a = MyWeek.objects.filter(take)


# Monthly Records


class MyMonth(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    month_date = models.DateField()
    fast = models.BooleanField(default=False)
    donation = models.BooleanField(default=False)
    ijtema = models.BooleanField(default=False)

    def __str__(self):
        return "{} - {}".format(self.user, self.take_month_name)

    @property
    def take_month_name(self):
        return self.month_date.strftime('%B %Y')

    @property
    def take_month_number(self):
        return self.month_date.month

    class Meta:
        verbose_name = 'Month'
        verbose_name_plural = 'Months'
        unique_together = ('user', 'month_date')


def validate_unique_month(sender, created, instance, *args, **kwargs):
    if MyMonth.objects.filter(month_date__month=instance.month_date.month,
                              month_date__year=instance.month_date.year).count() > 1:
        instance.delete()
        raise Http404


post_save.connect(validate_unique_month, sender=MyMonth)
