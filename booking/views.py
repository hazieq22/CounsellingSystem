from django.shortcuts import render,redirect
from booking.models import Student,Counsellor,Session,Detail
from django.db.models import Q
from django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate, login
# Create your views here.
def homepage(request):
    if request.method == 'POST':
        search2 = request.POST.get('search2')
        password = request.POST.get('password')

        try:
            student = Student.objects.get(studentID=search2)
            if student.studentPassword == password:
                request.session['search2'] = search2
                return redirect('home')
        except Student.DoesNotExist:
            pass

        try:
            counsellor = Counsellor.objects.get(counsellorID=search2)
            if counsellor.counsellorPassword == password:
                return redirect('appointment2')
        except Counsellor.DoesNotExist:
            pass

        return render(request, 'homepage.html', {'error_message': 'Invalid ID number or password'})
    else:
        search2 = request.session.get("search2", None)
        return render(request, "homepage.html", {'search2': search2})

def home(request):
    search2 = request.GET.get("search2")
    if search2:
        request.session['search2'] = search2
    else:
        search2 = request.session.get("search2")
    return render(request, "home.html", {'search2': search2})

def booking(request):
    if request.method == "POST":
        c_date = request.POST['date']
        c_time = request.POST['time']
        c_reason = request.POST['reason']
        search2 = request.GET.get("search2")
        if not search2:
            search2 = request.session.get("search2")

        if search2:
            student = Student.objects.get(studentID=search2)
            session = Session(studentID=student, date=c_date, time=c_time, reason=c_reason)
            session.save()
            
            dict = {
                'message': 'Data Saved'
            }
            return render(request, "booking.html", dict)
    else:
        dict ={
            'message' : ''
        }
        return render (request,"booking.html",dict)

def appointment(request):
    search2 = request.session.get("search2")
    if search2:
        post = Session.objects.filter(studentID=search2)
        try:
            student_profile = Student.objects.get(studentID=search2)
        except Student.DoesNotExist:
            student_profile = None
        return render(request, "appointment.html", {'posts': post,'student_profile': student_profile})
    else:
        return render(request, "error.html", {'message': 'Search2 is missing'})
    
def appointment2(request):
    if request.method == 'GET':
        post = Session.objects.all()
    return render(request, 'appointment2.html',{'posts':post})

def delete(request,sessionID):
  data = Session.objects.get(sessionID=sessionID)
  data.delete()
  return HttpResponseRedirect(reverse('appointment2'))

from django.shortcuts import render
from .models import Session, Detail  # Import your Session and Detail models

def update(request, sessionID):
    data = Session.objects.get(sessionID=sessionID)
    datak = Detail.objects.filter(sessionID=sessionID).first()  # Use .first() to avoid the exception

    context = {
        'data': data,
        'datak': datak,
    }

    return render(request, "update.html", context)


def update_data(request, sessionID):
    if request.method == 'POST':
        c_status = request.POST.get('status')

        if c_status is not None:
            data = Session.objects.get(sessionID=sessionID)
            data.status = c_status
            data.save()

    return HttpResponseRedirect(reverse("appointment2"))

def update2(request, sessionID):
    data = Session.objects.get(sessionID=sessionID)
    datak = Detail.objects.filter(sessionID=sessionID).first()

    context = {
        'data': data,
        'datak': datak,
    }

    return render(request, "update2.html", context)


from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import Session, Detail  

#def update_data2(request, sessionID):
    #if request.method == 'POST':
      #  c_details = request.POST['details']
      #  c_followup = request.POST['followup']

        #if c_details and c_followup is not None:
         #   session = Session.objects.get(sessionID=sessionID)
         #   studentID = session.studentID  

          #  datak = Detail(studentID=studentID, sessionID=session, details=c_details, followup=c_followup)
           # datak.save()

   # return HttpResponseRedirect(reverse("appointment2"))


def update_data2(request, sessionID):
    if request.method == 'POST':
        c_details = request.POST.get('details', '')
        c_followup = request.POST.get('followup', '')

        session = Session.objects.get(sessionID=sessionID)
        studentID = session.studentID  

        try:
            detail = Detail.objects.get(sessionID=session)
        except Detail.DoesNotExist:
            # If the Detail doesn't exist for this session, create a new one
            detail = Detail(sessionID=session, studentID=studentID)

        # Update the fields with new values
        detail.details = c_details
        detail.followup = c_followup

        detail.save()

    return HttpResponseRedirect(reverse("appointment2"))













