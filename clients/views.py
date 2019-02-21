from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from users.models import *
from company.models import *
from .models import *

# Create your views here.

@csrf_exempt
def show_clients(request):
    if request.method == 'GET':
        if request.user is not None:
            if not request.user.is_anonymous:
                print(request.user.is_anonymous)
                company = CompanyProfile.objects.get(user_id=request.user.id)
                clients = Client.objects.filter(company_id=company.id)
                context = {"user": request.user, "active": "Clients", "company": company, "clients": clients}
                return render(template_name='dashboard/clients.html', context=context, request=request)

        return HttpResponseRedirect("/signin/")

@csrf_exempt
def create_client(request):
    if request.method == 'GET':
        if request.user is not None:
            if not request.user.is_anonymous:

                company = CompanyProfile.objects.get(user_id=request.user.id)
                clients = Client.objects.filter(company_id=company.id)
                context = {"user": request.user, "active": "Clients", "company": company, "clients": clients}
                return render(template_name='dashboard/create_client.html', context=context, request=request)
            else:
                return HttpResponseRedirect("/signin/")
    elif request.method == 'POST':
        if request.user is not None:
            if not request.user.is_anonymous:
                company = CompanyProfile.objects.get(user_id=request.user.id)
                body = request.POST
                name = body['name']
                address = body['address']
                city = body['city']
                state = body['state']
                zip = body['zip']

                client = Client.objects.create(name=name, address=address, city=city, state=state, zip=zip, company_id=company.id)

                client.save()

                return HttpResponseRedirect('/clients/')
        return HttpResponseRedirect("/signin/")

