from django.shortcuts import render, redirect
from django.http import HttpResponse


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