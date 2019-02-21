from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from users.models import *
from company.models import *
from items.models import *
# Create your views here.

@csrf_exempt
def shows_invoices(request):
    if request.method == 'GET':
        if request.user is not None:
            if not request.user.is_anonymous:
                print(request.user.is_anonymous)
                company = CompanyProfile.objects.get(user_id=request.user.id)
                items = Item.objects.filter(company_id=company.id)

                context = {"user": request.user, "active": "Invoices", "company": company, "items": items}
                return render(template_name='dashboard/invoice.html', context=context, request=request)

        return HttpResponseRedirect("/signin/")
