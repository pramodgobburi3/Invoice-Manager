from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import *
from users.models import *
from .models import *


# Create your views here.

@csrf_exempt
def create_item(request):
    if request.method == 'GET':
        if request.user is not None:
            if not request.user.is_anonymous:

                context = {"user": request.user, "active": "New Item"}
                return render(template_name='dashboard/create_item.html', context=context, request=request)
            else:
                return HttpResponseRedirect("/signin/")
    elif request.method == 'POST':
        if request.user is not None:
            if not request.user.is_anonymous:

                body = request.POST
                company = CompanyProfile.objects.get(user_id=request.user.id)
                name = body['name']
                description = body['description']
                price = body['price']

                item = Item.objects.create(name=name, description=description, price=price, company_id=company.id)

                item.save()

                return HttpResponseRedirect('/')
        return HttpResponseRedirect("/signin/")
