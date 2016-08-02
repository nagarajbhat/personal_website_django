from django.conf.urls import url
from django.views.generic import ListView,DetailView
from projects.models import Post

urlpatterns = [
	url(r'^$', ListView.as_view(queryset=Post.objects.all().order_by('-date')[:25],
								template_name='projects/projects.html')),
	url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Post,
											 template_name='projects/post.html'))
]