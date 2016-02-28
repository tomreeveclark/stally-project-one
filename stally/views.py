from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from datetime import datetime

from stally.models import Market, Stall, UserProfile
from stally.forms import UserForm, UserProfileForm, MarketForm, StallForm

"""
Views Below:
"""

def index(request):
    
    markets = Market.objects.all()
    
    context_dict={'markets':markets}
    
    return render(request, 'stally/index.html', context_dict)

def markets(request):
    
    markets = Market.objects.all()
    
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        market_form = MarketForm(data=request.POST)

        # If the two forms are valid...
        if market_form.is_valid():
            # Save the user's form data to the database.
            market = market_form.save()

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print(market_form.errors)#, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        market_form = MarketForm()

    # Render the template depending on the context.
    return render(request,
            'stally/markets.html',
            {'market_form': market_form, 'markets': markets} )
    
def market(request, market_name_slug):
    
    context_dict={}
    
    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        market = Market.objects.get(slug=market_name_slug)
        context_dict['market_name'] = market.name
        context_dict['market_name_slug'] = market.slug

        # Retrieve all of the associated pages.
        # Note that filter returns >= 1 model instance.
        stalls = Stall.objects.filter(market=market)

        # Adds our results list to the template context under name pages.
        context_dict['stalls'] = stalls
        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['market'] = market
    except Market.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass
    
    return render(request, 'stally/market.html', context_dict)

def stall(request):
    
    stalls = Stall.objects.all()
    markets = Market.objects.all()
    
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        stall_form = StallForm(data=request.POST)

        # If the two forms are valid...
        if stall_form.is_valid():
            # Save the user's form data to the database.
            stall = stall_form.save()

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print(stall_form.errors)#, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        stall_form = StallForm()

    # Render the template depending on the context.
    return render(request,
            'stally/stall.html',
            {'stall_form': stall_form, 'stalls':stalls, 'markets': markets} )

def register(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            userprofile = profile_form.save(commit=False)
            userprofile.user = user
            userprofile.save()
            #profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            #if 'picture' in request.FILES:
            #    profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            userprofile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print(user_form.errors)#, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
            'stally/register.html',
            {'user_form': user_form, 'registered': registered} )

def login(request):
    
    context_dict={}
    
    return render(request, 'stally/login.html', context_dict)
