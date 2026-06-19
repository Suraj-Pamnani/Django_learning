from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from . models import student

def homepage(request):
    return render(request, "home.html")


def contact(request):
    return render(request, "contact.html")


def about(request):
    return render(request, "about.html")


def shop(request):
    return render(request, "shop.html")


def formpageprocess(request):
    a = int(request.POST['n1'])
    b = int(request.POST['n2'])

    total = a + b

    return HttpResponse("Sum = " + str(total))
 

def saveSession(request):
    request.session['username'] = "Suraj"
    return HttpResponse("Session Created")


def getSessionData(request):
    if request.session.has_key('username'):
        return HttpResponse(request.session['username'])
    else:
        return HttpResponse("Session Not Present")


def deleteSession(request):
    if request.session.has_key('username'):
        del request.session['username']

    return HttpResponse("Session Deleted")


# LOGIN

def loginpage(request):
    return render(request, 'login.html')


def loginprocess(request):

    txt1 = request.POST['email']

    request.session['myemail'] = txt1

    return redirect(dashboard)


def dashboard(request):

    if request.session.has_key('myemail'):

        return render(request, "dashboard.html")

    else:

        return redirect(loginpage)


def logout(request):

    if request.session.has_key('myemail'):
        del request.session['myemail']

    return redirect(loginpage)
def mailsenddemo(request):
 subject = 'Django Mail Demo'
 message = ' Hello How are you ?'
 email_from = settings.EMAIL_HOST_USER
 recipient_list = ['akash.padhiyar123@gmail.com',]
 send_mail( subject, message, email_from, recipient_list )
 return HttpResponse("Mail Sent")

def addstudentprocess(request):
    txt1 = request.POST['txt1']
    txt2 = request.POST['txt2']
    txt3 = request.POST['txt3']
    txt4 = request.POST['txt4']
    student.objects.create(name =txt1,mobile = txt2,email= txt3,address=txt4 )
    return HttpResponse("thank you")
def addstudentform(request):
    return render(request,'add-student.html')
def displayStudent(request):
    mystudentlist = student.objects.all()
    return render(request,'display-student.html',{'mydata': mystudentlist})

def deleteStudent(request, id):
    student.objects.get(id=id).delete()
    return redirect(displayStudent)