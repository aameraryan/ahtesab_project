from django.contrib import admin
from .models import User, MyDay, MyWeek, MyMonth

admin.site.register(User)
admin.site.register(MyDay)
admin.site.register(MyWeek)
admin.site.register(MyMonth)
