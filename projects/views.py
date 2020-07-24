from django.shortcuts import render, HttpResponse,redirect
from projects.models import Project, Message
from .forms import MessageForm
# Create your views here.
def project_index(request):
	projects = Project.objects.all()
	content = {
		'projects':projects
	}
	print(content)
	return render(request,'project_index.html',content)

def project_detail(request,pk):
	project = Project.objects.get(pk=pk)
	content = {
		'project':project
	}
	return render(request,'project_detail.html',content)

def contact(request):
	form = MessageForm()
	if request.method =='POST':
		form = MessageForm(request.POST)
		if form.is_valid():	
			form.save()
			
	return render(request, "contact.html", {"form":form})


