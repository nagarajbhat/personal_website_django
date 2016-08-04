from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request,'personal/home.html',{'typed':[1]})

def contact(request):
	return render(request,'personal/basic.html',{'content':['if you would like to contact me, here is my email','nagarajbhat12@gmail.com']})

def aboutme(request):
	return render(request,'personal/post.html',{'aboutme':['im a coomputer science graduate interested in coding and writing poems',]})






