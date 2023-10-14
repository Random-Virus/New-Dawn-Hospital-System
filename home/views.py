from django.shortcuts import render

# Create your views here.


   
def index(request):
    return render(request, 'home/index.html')
def appointment(request):

    return render(request, 'appointment/appointment.html')
def blog(request):

    return render(request, 'blog/index.html')
