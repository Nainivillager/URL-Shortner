from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone




def hello_world(request):
   return HttpResponse("Hello World!")

def home_page(request):

   context = {
      "submitted": False,
      "current_date": timezone.now().date()
   }

   if (request.method) == 'POST':

      context["submitted"] = True

      data = request.POST
      long_url = data['longurl']
      custom_name = data['custom_name']

      print(long_url)
      print(custom_name)

      context["long_url"] = long_url
      context["short_url"] = request.build_absolute_uri() + custom_name

      
   else:
      print("No data sent by user")

   

   return render(request, "index.html", context)


# def task_page(request):
#    return render(request, "task.html")
# Create your views here.
