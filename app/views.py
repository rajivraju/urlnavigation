from django.shortcuts import render

# Create your views here.
def url1(request):
    return render(request,'url.html')
def url2(request):
    return render(request,'url2.html')