"""broomtrade URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib.auth.decorators import permission_required
from blog.views import BlogListView, BlogDetailView, BlogCreate, BlogUpdate, \
BlogDelete


urlpatterns = [
    url(r'^$', BlogListView.as_view(), name="blog_index"),
    url(r'^(?P<pk>\d+)/detail/$', BlogDetailView.as_view(), name="blog_detail"),
    url(r'^add/$', permission_required("blog.add_blog")\
        (BlogCreate.as_view()), name="blog_add"),
    url(r'^(?P<pk>\d+)/edit/$', permission_required("blog.change_blog")\
        (BlogUpdate.as_view()), name="blog_edit"),
    url(r'^(?P<pk>\d+)/delete/$', permission_required("blog.delete_blog")\
        (BlogDelete.as_view()), name="blog_delete"),
]
