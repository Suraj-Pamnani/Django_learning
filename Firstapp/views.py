from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return render(request,"home.html")
def contact(request):
    return render(request,"contact.html")
def about(request):
    return render(request,"about.html")
def shop(request):
    return render(request,"shop.html")
def formpageprocess(request):
  a = int(request.POST['n1'])
  b = int(request.POST['n2'])
  sum = a + b
  ans = "A is ",a , " and B is ",b, " sum is ",sum
  d = ""
  if sum ==100:
    d = "if triggred"
  elif sum<100:
    d = "elif triggred"
  else :
    d = "else triggred"
  return render(request,'ans.html',{'mya':a,'myb':b,'mysum':sum,'myd':d})


