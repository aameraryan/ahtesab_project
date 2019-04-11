from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from .models import MyDay, MyMonth, MyWeek
from .forms import DayAddForm, DayUpdateForm, MonthAddForm, MonthUpdateForm, WeekAddForm
import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def home(request):
    return render(request, 'portal/home.html')


@login_required
def daily(request):
    context = {'days': request.user.myday_set.all()}
    return render(request, 'portal/daily.html', context)


def day_add(request):
    if request.method == "POST":
        form = DayAddForm(request.POST)
        if form.is_valid():
            temp_form = form.save(commit=False)
            temp_form.user = request.user
            temp_form.save()
            messages.success(request, 'Day Added Succesfully.')
            return redirect('daily')
        else:
            form = DayAddForm()
    else:
        form = DayAddForm()
    return render(request, 'portal/day_add.html', {'form': form})


def day_update(request, u_day, u_month, u_year):
    try:
        day_instance = request.user.myday_set.get(day_date__day=u_day, day_date__month=u_month, day_date__year=u_year)
        if request.method == 'POST':
            print('post')
            form = DayUpdateForm(data=request.POST, instance=day_instance)
            if form.is_valid():
                print('valid')
                form.save()
                messages.success(request, "Day updated succesfully.")
                return redirect('daily')
            else:
                form = DayUpdateForm(day_instance=day_instance)
                messages.warning(request, 'Form Invalid')
        else:
            form = DayUpdateForm(day_instance=day_instance)
        return render(request, 'portal/day_update.html', {'form': form})
    except ObjectDoesNotExist:
        return HttpResponse('No record with this date..')


# Monthly Records


@login_required
def monthly(request):
    context = {'months': request.user.mymonth_set.all()}
    return render(request, 'portal/monthly.html', context)


def month_add(request):
    if request.method == "POST":
        form = MonthAddForm(request.POST)
        if form.is_valid():
            temp_form = form.save(commit=False)
            temp_form.user = request.user
            temp_form.save()
            messages.success(request, 'Month Added Succesfully.')
            return redirect('monthly')
        else:
            form = MonthAddForm()
    else:
        form = MonthAddForm()
    return render(request, 'portal/month_add.html', {'form': form})


def month_update(request, u_month, u_year):

        month_instance = request.user.mymonth_set.get(month_date__month=u_month, month_date__year=u_year)
    # try:
        if request.method == 'POST':
            form = MonthUpdateForm(data=request.POST, instance=month_instance)
            if form.is_valid():
                form.save()
                messages.success(request, 'Month updated succefully')
                return redirect('monthly')
            else:
                form = MonthUpdateForm(month_instance=month_instance)
        else:
            form = MonthUpdateForm(month_instance=month_instance)
        return render(request, 'portal/month_update.html', {'form': form})

    # except ObjectDoesNotExist:
    #     raise Http404


@login_required
def weekly(request):
    context = {'weeks': request.user.myweek_set.all()}
    return render(request, 'portal/weekly.html', context)


@login_required
def week_add(request):
    if request.method == "POST":
        form = WeekAddForm(request.POST)
        if form.is_valid():
            temp_form = form.save(commit=False)
            temp_form.user = request.user
            temp_form.save()
            messages.success(request, 'Week Added Succesfully.')
            return redirect('weekly')
        else:
            form = WeekAddForm()
    else:
        form = WeekAddForm()
    return render(request, 'portal/week_add.html', {'form': form})
