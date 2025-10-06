from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from service.models import  *
from django.core.exceptions import ObjectDoesNotExist
import pickle
import numpy as np

@login_required
def Home(request):
    return render(request,'Home.html', {})

def Register(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        phno = request.POST.get('number')
        password = request.POST.get('password')

        new_user = User.objects.create_user(name, email, password)
        new_user.phno = phno

        new_user.save()
        return redirect('loginpage')
    return render(request,'Register.html', {})

def Login(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('Error, user does not exist')
    return render(request,'Login.html', {})

def logoutuser(request):
    logout(request)
    return redirect('loginpage')

def Aboutus(request):
    return render(request,'Aboutus.html', {})

def Services(request):
    return render(request,'Services.html', {})

def Contactus(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        messages = request.POST['add']
        ins = Contact(username=username,add=messages, email=email)
        ins.save()
        print("ok")
    return render(request,'Contactus.html', {})

def Patientde(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        lastname = request.POST['lastname']
        gender = request.POST['gender']
        date_of_birth = request.POST['date_of_birth']
        marital_status = request.POST['marital_status']
        bloodgroup = request.POST['bloodgroup']
        aadharnumber = request.POST['aadharnumber']
        email = request.POST['email']
        phonenumber = request.POST['phonenumber']
        add = request.POST['add']
        symptoms = request.POST['symptoms']
        ename = request.POST['ename']
        relation = request.POST['relation']
        emergencynumber = request.POST['emergencynumber']
        ins = Patient(first_name=first_name, lastname=lastname, gender=gender, date_of_birth=date_of_birth, marital_status=marital_status, bloodgroup=bloodgroup, aadharnumber=aadharnumber, email=email, phonenumber=phonenumber, add=add, symptoms=symptoms, ename=ename, relation=relation, emergencynumber=emergencynumber)
        ins.save()
        print("ok")
    return render(request,'Patient.html', {})

def Doctordetails(request):
    if request.method == "POST":
        dname = request.POST['dname']
        specialization = request.POST['specialization']
        gender = request.POST['gender']
        email = request.POST['email']
        phonenumber = request.POST['phonenumber']
        
        ins = Doctor(dname=dname, specialization=specialization, gender=gender,email=email, phonenumber=phonenumber)
        ins.save()
    return render(request,'Doctor.html', {})

def Doctor_info(request):
    # Query the database to retrieve all DoctorInformation objects
    doctors = Doctor.objects.all()

    # Pass the retrieved data to the template
    context = {'doctors': doctors}
    return render(request, 'doctor_info.html', context)

def Appointmentdetails(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        phoneNo = request.POST.get('phoneNo')
        appointmentDate = request.POST.get('appointmentDate')
        symptoms = request.POST.get('symptoms')

        new_appointment = Apps.objects.create(
            name=name,
            age=age,
            phoneNo=phoneNo,
            appointmentDate=appointmentDate,
            symptoms=symptoms
        )

        # You can add additional logic here if needed

        return redirect('appointment')
    return render(request, 'Appointment.html', {})

def Priscription(request):
    # Fetch only approved appointments
    approved_appointments = Apps.objects.filter(is_approved=True)

    context = {'approved_appointments': approved_appointments}
    return render(request, 'Priscription.html', context)

def Feedback(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        messages = request.POST['msg']
        ins = Feed(name=name,msg=messages, email=email)
        ins.save()
        print("ok")
    return render(request,'Feedback.html', {})

RF_pkl_filename = 'RandomForest.pkl'  # Replace with the path to your .pkl file
with open(RF_pkl_filename, 'rb') as Model_pkl:
    loaded_model = pickle.load(Model_pkl)

def predict(request):
    return render(request,'prediction.html',{})

def prediction(request):
    result = None
    if request.method == 'POST':
        # Retrieve user input from the frontend form
        Fever = request.POST['Fever']
        if Fever == "yes":
            Fever = 1
        elif Fever == "no":
            Fever = 0

        Shortness_of_breath = request.POST['Shortness of breath']
        if Shortness_of_breath == "yes":
            Shortness_of_breath = 1
        elif Shortness_of_breath == "no":
            Shortness_of_breath = 0

        Cough = request.POST['Cough']
        if Cough == "yes":
            Cough = 1
        elif Cough == "no":
            Cough = 0

        Chest_pain = request.POST['Chest pain']
        if Chest_pain == "yes":
            Chest_pain = 1
        elif Chest_pain == "no":
            Chest_pain = 0

        Vomitting = request.POST['Vomitting']
        if Vomitting == "yes":
            Vomitting = 1
        elif Vomitting == "no":
            Vomitting = 0

        Sweating = request.POST['Sweating']
        if Sweating == "yes":
            Sweating = 1
        elif Sweating == "no":
            Sweating = 0

        Sudden_weakness = request.POST['Sudden weakness']
        if Sudden_weakness == "yes":
            Sudden_weakness = 1
        elif Sudden_weakness == "no":
            Sudden_weakness = 0

        Numbness = request.POST['Numbness']
        if Numbness == "yes":
            Numbness = 1
        elif Numbness == "no":
            Numbness = 0

        Headache = request.POST['Headache']
        if Headache == "yes":
            Headache = 1
        elif Headache == "no":
            Headache = 0

        Swelling = request.POST['Swelling']
        if Swelling == "yes":
            Swelling = 1
        elif Swelling == "no":
            Swelling = 0

        Diarrhea = request.POST['Diarrhea']
        if Diarrhea == "yes":
            Diarrhea = 1
        elif Diarrhea == "no":
            Diarrhea = 0

        Cancer = request.POST['Cancer']
        if Cancer == "yes":
            Cancer = 1
        elif Cancer == "no":
            Cancer = 0

        # Add more fields as needed

        # Prepare the input data for prediction
        input_data = [Fever, Shortness_of_breath, Cough, Chest_pain, Vomitting,Sweating, Sudden_weakness, Numbness, Headache, Swelling, Diarrhea, Cancer]  # Adjust this according to your model's input features
        input_data_as_array = np.asarray(input_data)
        input_data_reshaped = input_data_as_array.reshape(1, -1)

        # Make prediction using the loaded model
        prediction = loaded_model.predict(input_data_reshaped)
        
    return render(request, 'prediction.html', {})
