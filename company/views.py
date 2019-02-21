from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import *
from users.models import *

# Create your views here.
@csrf_exempt
def create_compnay(request):
    if request.method == "GET":
        if request.user is not None:
            if not request.user.is_anonymous:
                context = {"user": request.user}
                return render(template_name='create_company.html', request=request)
        return HttpResponseRedirect("/signin/")
    if request.method == "POST":
        if request.user is not None:
            if not request.user.is_anonymous:
                body = request.POST
                name = body['name']
                address = body['address']
                city = body['city']
                state = body['state']
                zip = body['zip']
                phone = body['phone']
                user_id = request.user.id

                company = CompanyProfile.objects.create(name=name, address=address,
                                                        city=city, state=state, zip=zip,
                                                        business_phone=phone, user_id=user_id)

                company.save()

                return HttpResponseRedirect("/")

        return HttpResponseRedirect("/signin/")

