from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from .models import CarDealer, CarMake, CarModel
from .restapis import get_dealers_from_cf, get_dealer_reviews_from_cf
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.
def index(request):
    return render(request, 'djangoapp/index.html')


# Create an `about` view to render a static about page
def about(request):
    return render(request,'djangoapp/about.html')
    
# Create a `contact` view to return a static contact page
def contact(request):
    return render(request, 'djangoapp/contact.html' )

# Create a `login_request` view to handle sign in request
def login_request(request):
   if request.method== "POST":
        username=request.POST['username']
        password=request.POST['psw']
        user=authenticate(username=username,password=password)
   if user is not None:
        login(request,user)
        return redirect('djangoapp:index')
           
   else:
        return render(request, 'djangoapp/registration.html', {})


# Create a `logout_request` view to handle sign out request
def logout_request(request):
    print("Log out the user `{}`".format(request.user.username))
    logout(request)
    return redirect('djangoapp:index')


# Create a `registration_request` view to handle sign up request
def registration_request(request):
    if request.method=="GET":
        return render(request,'djangoapp/registration.html',{})
    
    elif request.method=="POST":
            username = request.POST['username']
            password = request.POST['psw']
            first_name = request.POST['firstname']
            last_name = request.POST['lastname']
            user_exist = False
            try:
                User.objects.get(username=username)
                user_exist=true
            except :
                  logger.debug("{} is new user".format(username))
    if not user_exist:

            # Create user in auth_user table
                    user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                            password=password)
 
                    login(request, user)
                    return redirect('djangoapp:index')
    
    else:
        return render(request, 'djangoapp/registration.html', {})


# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    if request.method == "GET":
        context = {}
        url = "https://cf61a9d5.eu-gb.apigw.appdomain.cloud/dealerships/dealerships"
        # Get dealers from the URL
        dealerships_list = get_dealers_from_cf(url)
        # Concat all dealer's short name
        # Return a list of dealer short name
        context = {"dealerships_list": dealerships_list}
        return render(request, 'djangoapp/index.html', context)


# Create a `get_dealer_details` view to render the reviews of a dealer
def get_dealer_details(request, dealer_id):
    if request.method == "GET":
        url = "https://cf61a9d5.eu-gb.apigw.appdomain.cloud/get_reviews/get_reviews?dealerId=" + \
            str(dealer_id)
        # Get dealers from the URL
        reviews_list = get_dealer_reviews_from_cf(url)
        # Concat all dealer's short name
        context = {"reviews_list": reviews_list, "dealer_id": dealer_id}
        return render(request, 'djangoapp/dealer_details.html', context)



# Create a `add_review` view to submit a review
# def add_review(request, dealer_id):
# ...

