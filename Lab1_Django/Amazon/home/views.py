from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def welcome(req,name):
    # name=req.GET[]
    x={}
    x["a"]=name
    return HttpResponse (f"<h1> Welcome {name} </h1>")
