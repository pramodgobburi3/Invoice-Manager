from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from company.models import CompanyProfile
from .models import *
from django.shortcuts import redirect
from items.models import *

# Create your views here.

@csrf_exempt
def web_login(request):
    if request.method == 'GET':
        return render_to_response('authenticate/login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            context = {"user": user}

            businesses = CompanyProfile.objects.filter(user_id=user.id)
            print(businesses)
            if not businesses:
                return HttpResponseRedirect("/register_business/")
            return HttpResponseRedirect("/")
        else:
            context = {"error": True}
            return render_to_response('authenticate/login.html', context=context)

@csrf_exempt
def dashboard(request):
    if request.method == 'GET':
        if request.user is not None:
            if not request.user.is_anonymous:
                print(request.user.is_anonymous)
                company = CompanyProfile.objects.get(user_id=request.user.id)
                items = Item.objects.filter(company_id=company.id)
                context = {"user": request.user, "active": "Dashboard", "company": company, "items": items}
                return render(template_name='dashboard/dashboard.html', context=context, request=request)
            else:
                return HttpResponseRedirect("/signin")

@csrf_exempt
def register(request):
    if request.method == "GET":
        if request.user is not None:
            if not request.user.is_anonymous:
                context = {"user": request.user}
                return HttpResponseRedirect("/")
        return render(template_name='authenticate/register.html', request=request)
    elif request.method == "POST":
        body = request.POST
        username = body['username']
        firstname = body['firstname']
        lastname = body['lastname']
        password = body['password']
        email = body['email']

        new_user = User.objects.create_user(username=username, email=email, password=password,
                                            first_name=firstname, last_name=lastname)
        profile = UserProfile.objects.get(user=new_user)
        profile.fistname = firstname
        profile.lastname = lastname
        profile.email = email
        profile.save()
        return HttpResponseRedirect("/register_company/")

@csrf_exempt
def web_logout(request):
    logout(request)
    return HttpResponseRedirect("/signin/")