from django.urls import path
from . import views

urlpatterns = [

    path('', views.homepage),
    path('home/', views.homepage),
    path('about/', views.about),
    path('contact/', views.contact),
    path('shop/', views.shop),

    path('contactprocess/', views.formpageprocess),

    path('saveSession/', views.saveSession),
    path('getSession/', views.getSessionData),
    path('removeSession/', views.deleteSession),

    path('login/', views.loginpage),
    path('loginprocess/', views.loginprocess),
    path('dashboard/', views.dashboard),
    path('logout/', views.logout),

    path('maildemo/',views.mailsenddemo),
    path('addstudentForm/',views.addstudentform),
    path('addstudentprocess/',views.addstudentprocess),
    path('display-student/',views.displayStudent),
    path('delete-student/<int:id>',views.deleteStudent), 

]