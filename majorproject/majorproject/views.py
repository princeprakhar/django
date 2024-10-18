from django.http import HttpResponse
from django.shortcuts import render

def home(response:HttpResponse)->render:
    return render(response,"index.html")



def about(response:HttpResponse)->render:
    return render(response,"about.html")