import csv
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Count
from django.http import HttpResponse
from .models import User, Event, Registration
from .forms import VolunteerSignUpForm
from django.contrib.auth.decorators import login_required


@login_required
def event_list(request):
    events = Event.objects.all().order_by('date')
    return render(request, 'core/event_list.html', {'events': events})

def logout_view(request):
    logout(request)
    return redirect('login')


# AUTHENTICATION VIEWS


def register_volunteer(request):
    if request.method == 'POST':
        form = VolunteerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('event_list')
    else:
        form = VolunteerSignUpForm()
    return render(request, 'core/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.is_coordinator or user.is_superuser:
                return redirect('admin_dashboard')
            return redirect('event_list')
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form})



# DASHBOARD & ADMIN VIEWS

def is_admin_or_coordinator(user):
    return user.is_superuser or user.is_coordinator


@user_passes_test(is_admin_or_coordinator)
def admin_dashboard(request):
    # Aggregating data for the dashboard cards
    total_volunteers = User.objects.filter(is_volunteer=True).count()
    events = Event.objects.annotate(attendee_count=Count('attendees'))
    
    context = {
        'total_volunteers': total_volunteers,
        'events': events,
    }
    return render(request, 'core/dashboard.html', context)



# REPORTING VIEWS


@user_passes_test(is_admin_or_coordinator)
def export_volunteer_report(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="volunteer_report.csv"'

    writer = csv.writer(response)
    writer.writerow(['Volunteer Username', 'Email', 'Event Title', 'Registration Date', 'Attended'])

    registrations = Registration.objects.select_related('volunteer', 'event').all()
    for reg in registrations:
        writer.writerow([
            reg.volunteer.username,
            reg.volunteer.email,
            reg.event.title,
            reg.registered_at.strftime('%Y-%m-%d'),
            reg.attended
        ])

    return response