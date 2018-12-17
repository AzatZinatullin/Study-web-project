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
from news.views import NewsListView, NewDetailView, NewCreate, NewUpdate, NewDelete, RssNewsListFeed, AtomNewsListFeed

urlpatterns = [
    url(r'^$', NewsListView.as_view(), name="news_index"),
    url(r'^(?P<pk>\d+)/detail/', NewDetailView.as_view(), name="news_detail"),
    url(r'^add/$', permission_required("news.add_new")\
        (NewCreate.as_view()), name="news_add"),
    url(r'^(?P<pk>\d+)/edit/', permission_required("news.change_new")\
        (NewUpdate.as_view()), name="news_edit"),
    url(r'^(?P<pk>\d+)/delete/', permission_required("news.delete_new")\
        (NewDelete.as_view()), name="news_delete"),
    url(r'feed/rss/$', RssNewsListFeed(), name = "news_feed_rss"),
    url(r'feed/atom/$', AtomNewsListFeed(), name = "news_feed_atom"),
]
