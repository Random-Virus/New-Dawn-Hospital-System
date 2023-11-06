from django.shortcuts import render, redirect
from .forms import ambulanceRequestForm
from .models import ambulanceRequest, Hospital
from django.contrib.auth.decorators import login_required
from geopy.distance import geodesic
from django.http import JsonResponse
from django.db.models.functions import TruncHour
from django.db.models import Count
# from .models import HeatmapData
# Create your views here.

@login_required
def ambulanceRequestView(request):

    if request.method == 'POST':
        form = ambulanceRequestForm(request.POST)
        if form.is_valid():
            ambulance_request = form.save(commit=False)
           
            ambulance_request.user = request.user.get_full_name()
            ambulance_request.save()
            

            return redirect('hospital_nearest')
    else:
        print('Please enter the details')
        form = ambulanceRequestForm()

    return render(request, 'ambulance/ambulanceRequest.html', {'form': form})

def find_nearest_hospital(request):
    user_location = ambulanceRequest.objects.latest('timestamp')
    user_coordinates = (user_location.latitude, user_location.longitude)
    print(user_coordinates)
    hospitals = Hospital.objects.all()
    nearest_hospital = None
    min_distance = None

    for hospital in hospitals:
        hospital_coordinates = (hospital.latitude, hospital.longitude)
        distance = geodesic(user_coordinates, hospital_coordinates).kilometers
        print('hospital')
        print(hospital_coordinates)
        if min_distance is None or distance < min_distance:
            min_distance = distance
            nearest_hospital = hospital
    # print(distance)

    context = {
        'hospital_latitude': nearest_hospital.latitude,
        'hospital_longitude': nearest_hospital.longitude,
        'hospital': nearest_hospital,
        'distance': min_distance
    }
    print(nearest_hospital.latitude)
    print(nearest_hospital.longitude)
    return render(request, 'ambulance/nearest_hospital.html', context)


def viewRequests(request):
    
    requests = ambulanceRequest.objects.all()
    context = {
        'requests': requests
    }

    print(ambulanceRequest.objects.get(pk=1).user)
    return render(request, 'ambulance/viewRequests.html', context)

def request_detail(request, request_id):
    ambulance_request = ambulanceRequest.objects.get(id=request_id)
    context = {
        'ambulance_request': ambulance_request
    }
    return render(request, 'ambulance/request_detail.html', context)


def dashboard(request):
    return render(request, 'ambulance/dashboard.html')

def ambulance_request_count(request):
    data = ambulanceRequest.objects.annotate(hour=TruncHour('timestamp')).values('hour').annotate(count=Count('id')).order_by('hour')
    print(data)
    return JsonResponse(list(data), safe=False)

