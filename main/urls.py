from django.urls import path
from django.conf.urls import url
from . import views
from . views import(PostCreateView,)
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('',views.index, name="home"),
	path('Css/',views.Css, name='css'),
	path('technology/',views.technology, name='technology'),
	path('javascript/',views.javascript, name='javascript'),
	path('django/',views.django, name='django'),
	path('Css/',views.Css, name='css'),
	path('HTML/',views.Html, name='html'),
	path('time/',views.time, name='time'),
	path('<int:pk>/',views.detail, name='detail'),
	path('post/new/', PostCreateView.as_view(), name='post-create'),
	#path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
	#path('sign/',views.sign, name='sign'),
	#path('logout/', auth_views.LogoutView.as_view(template_name='main/logout.html'), name='logout'),
]