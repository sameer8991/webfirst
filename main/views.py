from django.shortcuts import render,redirect
from .models import Post
from .forms import UserRegisterForm
import sys
from django.contrib import messages
#from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from main.models import Post, Comment
from main.forms import CommentForm

# Create your views here.
#@login_required
def index(request):
	posts=Post.objects.all().order_by('-date_posted')
	params = {'post':posts}
	return  render(request,'main/index.html',params)


def technology(request):
	posts = Post.objects.filter(categary = 'technology').order_by('-date_posted')
	params = {'post':posts}
	return  render(request,'main/technology.html',params)


def Css(request):
	return  render(request,'main/Css.html')

def time(request):
	return  render(request,'main/time.html')


def django(request):
	posts = Post.objects.filter(categary = 'Django').order_by('-date_posted')
	params = {'post':posts}
	return  render(request,'main/django.html',params)



def Html(request):
	posts = Post.objects.filter(categary = 'Html').order_by('-date_posted')
	params = {'post':posts}
	print(params)
	return  render(request,'main/HTML.html',params)


def javascript(request):
	return  render(request,'main/javascript.html')


class PostCreateView(LoginRequiredMixin,CreateView):
	model = Post
	template_name = 'main/post_new.html'
	success_url = '/main'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def get_context_data(self,**kwargs):
		data = super().get_context_data(**kwargs)
		data['tag_line'] = 'add a new post'
		return data


"""def sign(request):
	if request.method=='POST':
		form =UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}.')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return  render(request,'main/sign.html',{'form':form})"""



def detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)

    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()

    context = {"post": post, "comments": comments, "form": form}
    return render(request, "main/detail.html", context)

