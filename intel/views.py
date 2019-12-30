from django.shortcuts import render
from django.http import HttpResponse
from intel.models import Comments
# Create your views here.
def home(request):
	a = Comments.objects.all()
	return render (request,'res.html',{'a1':a})

# Basic calculator code
def add(request):
	num1 = int(request.POST["num1"])
	oper = request.POST["oper"]
	num2 = int(request.POST["num2"])
	if oper=="+":
		c = num1+num2
		return render (request,'page.html',{'result':c})
	elif oper =="-":
		c=num1-num2
		return render (request,'page.html',{'result':c})
	elif oper =="*":
		c =num1*num2
		return render (request,'page.html',{'result':c})
	elif oper == "/":
		c= num1/num2
		return render (request,'page.html',{'result':c})
	elif oper =="//":
		c=num1//num2
		return render (request,'page.html',{'result':c})
	elif oper =="%":
		c=num1%num2
		return render (request,'page.html',{'result':c})
	else :
		c = 'give proper operator'
		return render (request,'page.html',{'result':c})




def comme(request):
		a = Comments.objects.all()

		return render(request,'comment.html',{'eee':a})

def pose(request):
		name = request.POST.get("name")
		comnts = request.POST.get("comment")
		# stores the values in database
		Comments.objects.create(name=name,comnts=comnts) 
		return render(request,'aa.html')
