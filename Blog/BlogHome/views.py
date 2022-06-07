from django.shortcuts import render

#-----------------------------------------------------------------------------------------------------------------------------------------------

def home(request):
    return render(request, "BlogHome/home.html")

def aboutme(request):
    return render(request, "BlogHome/about.html")
