from django.shortcuts import render

def index(request):
	return render(request, 'personal/home.html')

def contact(request):
    return render(request, 'personal/basic.html', {'contentnya':['if you like contact me, please contact me','yasirutomo@gmail.com']})
