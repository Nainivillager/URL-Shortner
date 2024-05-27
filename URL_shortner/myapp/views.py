from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import LongToShort

def home_page(request):

   context = {
      "submitted": False,
      "current_date": timezone.now().date(),
      "error": False
   }

   if (request.method) == 'POST':

      context["submitted"] = True

      data = request.POST
      long_url = data['longurl']
      custom_name = data['custom_name']

      try:
      # CREATE
         obj = LongToShort(long_url = long_url, short_url = custom_name)
         obj.save()
      
      # READ
         clicks = obj.clicks
         context["long_url"] = long_url
         context["short_url"] = request.build_absolute_uri() + custom_name
         context["clicks"] = clicks
      except:
         context["error"] = True
      
   else:
      print("No data sent by user")

   

   return render(request, "index.html", context)

def redirect_url(request,short_url):
   row = LongToShort.objects.filter(short_url = short_url)
   if len(row) == 0:
      return HttpResponse("No such short Url exist")
   obj = row[0]
   long_url = obj.long_url

   obj.clicks = obj.clicks + 1
   obj.save()

   return redirect(long_url)