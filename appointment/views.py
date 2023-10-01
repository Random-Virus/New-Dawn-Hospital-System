from django.shortcuts import render, redirect
from .forms import AppointmentForm, confirmForm
# Create your views here.
def appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
       
        if form.is_valid():
            form.save()
            print(form.errors)
            print('Error')
            return redirect('index') 
    else:
        form = AppointmentForm()
        
    context = {
        'form': form,
       
        }
    return render(request, 'appointment/appointment.html', context)

def view_appointments(request):
    appointments = Appointment.objects.all()
    if request.method == 'POST':
        form = confirmForm(request.POST)
        if form.is_valid():
            appointments.doctor = form.cleaned_data['doctor']
            appointments.save()
            print('Appointments saved')
    else:
        form = confirmForm()
        print('Appointments not saved')
    context = {
        'appointments': appointments,
        'form': form
        }
    return render(request, 'appointment/view_appointments.html', context)

def appointment_details(request, request_number):
    appointments = get_object_or_404(Appointment, request_number=request_number)

    if request.method == 'POST':
        form = confirmForm(request.POST)
        if form.is_valid():
            appointments.doctor = form.cleaned_data['doctor']
            appointments.save()
            print('Appointments saved')
    else:
        form = confirmForm()
        print('Appointments not saved')
    context = {
        'appointments': appointments
        }
    
    return render(request, 'appointment/appointment_details.html', context)


def confirm_appointment(request, request_number):
    appointments = get_object_or_404(Appointment, request_number=request_number)
    if 'doctor' in request.POST:
        doctor_id = request.POST.get('doctor')
        doctor = get_object_or_404(Doctor, id=doctor_id)

        appointments.doctor = doctor
        appointments.save()
        print('Appointments saved')
    else:
        print("Two")
    messages.success(request, 'Appointment confirmed successfully!')
    return redirect('view_appointments')