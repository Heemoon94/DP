from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home1(req) :
	return HttpResponse(
	"<h1>Hello World~!!<h/1>"
	)

def home(req) :
	return render(req, "Home.html",{"a":"Good","b":"afternoon"})
