from django.conf.urls import url,include
from . import views
from django.views.generic import ListView,DetailView
from personal.models import Post
urlpatterns = [
	url(r'^$',views.index,name='index'),
	url(r'^contact/',views.contact,name='contact'),
	# url(r'^aboutme/$',views.aboutme,name='aboutme'),
	# url(r'^aboutme/$', ListView.as_view(queryset=Post.objects.all().order_by('-date')[:25],
	# 							template_name='personal/header.html')),
	url(r'^aboutme/(?P<pk>\d+)/$', DetailView.as_view(model=Post,
											 template_name='personal/post.html'))]