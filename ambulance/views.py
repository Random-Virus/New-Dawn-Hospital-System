from django.shortcuts import render, redirect
from .forms import ambulanceRequestForm
from .models import ambulanceRequest, Hospital
from django.contrib.auth.decorators import login_required
from geopy.distance import geodesic
# Create your views here.

@login_required
def ambulanceRequestView(request):

    if request.method == 'POST':
        form = ambulanceRequestForm(request.POST)
        if form.is_valid():
            ambulance_request = form.save(commit=False)
           
            ambulance_request.user = request.user
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
    print(distance)

    context = {
        'hospital': nearest_hospital,
        'distance': min_distance
    }
    return render(request, 'ambulance/nearest_hospital.html', context)
