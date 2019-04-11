from django import forms
from .models import MyDay, MyWeek, MyMonth


class DayAddForm(forms.ModelForm):

    # day_date = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = MyDay
        exclude = ('user',)


class DayUpdateForm(forms.ModelForm):

    def __init__(self, day_instance=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if day_instance is not None:
            self.fields['day_date'].initial = day_instance.day_date
            self.fields['day_date'].widget.attrs['readonly'] = 'readonly'
            self.fields['tahajjud'].initial = day_instance.tahajjud
            self.fields['fajar'].initial = day_instance.fajar
            self.fields['zuhar'].initial = day_instance.zuhar
            self.fields['asar'].initial = day_instance.asar
            self.fields['maghrib'].initial = day_instance.maghrib
            self.fields['isha'].initial = day_instance.isha
            self.fields['tilawat'].initial = day_instance.tilawat
            self.fields['zikr'].initial = day_instance.zikr

    class Meta:
        model = MyDay
        exclude = ('user',)


# Monthly Records


class MonthAddForm(forms.ModelForm):

    class Meta:
        model = MyMonth
        exclude = ('user',)


class MonthUpdateForm(forms.ModelForm):

    def __init__(self, month_instance=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if month_instance is not None:
            self.fields['month_date'].initial = month_instance.month_date
            self.fields['month_date'].widget.attrs['readonly'] = 'readonly'
            self.fields['fast'].initial = month_instance.fast
            self.fields['donation'].initial = month_instance.donation
            self.fields['ijtema'].initial = month_instance.ijtema

    class Meta:
        model = MyMonth
        exclude = ('user', )


class WeekAddForm(forms.ModelForm):

    class Meta:
        model = MyWeek
        exclude = ('user',)

