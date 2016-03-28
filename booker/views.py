from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from datetime import datetime

from django.contrib.auth.models import User
from booker.models import Market, Stall, UserProfile, Booking, Application, Event
from booker.forms import ApplicationForm

def index(request):
    
    markets = Market.objects.all()
    
    context_dict={'markets':markets}
    
    return render(request, 'booker/index.html', context_dict)

def stallowner(request):
    
    markets = Market.objects.all()
    
    context_dict={'markets':markets}
    
    return render(request, 'booker/stallowner.html', context_dict)

def marketowner(request):
    
    markets = Market.objects.all()
    
    context_dict={'markets':markets}
    
    return render(request, 'booker/marketowner.html', context_dict)

def application(request):
    stalls = Stall.objects.all()
    markets = Market.objects.all()
    
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        application_form = ApplicationForm(data=request.POST)

        # If the forms is valid...
        if application_form.is_valid():
            # Save the user's form data to the database - this 'application' can be called whatever, it is just creating an object
            application = application_form.save()
            #application.save()

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print(application_form.errors)#, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        application_form = ApplicationForm()

    # Render the template depending on the context.
    return render(request,
            'booker/application.html',
            {'application_form': application_form, 'markets':markets, 'stalls':stalls})
