from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
   return HttpResponse("Hello World!")

def home_page(request):
   if (request.method) == 'POST':
      data = request.POST
      long_url = data['longurl']
      custom_name = data['custom_name']

      print(long_url)
      print(custom_name)
   else:
      print("No data sent by user")

   return render(request, "index.html")


# def task_page(request):
#    return render(request, "task.html")
# Create your views here.
