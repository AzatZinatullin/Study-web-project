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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import permission_required
from goods.views import GoodsListView, GoodDetailView, GoodCreate, GoodUpdate, \
GoodDelete, RssGoodsListFeed, AtomGoodsListFeed


urlpatterns = [
    url(r'^(?P<pk>\d+)/list/', GoodsListView.as_view(), name="goods_index"),
    url(r'^(?P<pk>\d+)/detail/', GoodDetailView.as_view(), name="goods_detail"),
    url(r'^(?P<pk>\d+)/add/', permission_required("goods.add_good")\
        (GoodCreate.as_view()), name="goods_add"),
    url(r'^(?P<pk>\d+)/edit/', permission_required("goods.change_good")\
        (GoodUpdate.as_view()), name="goods_edit"),
    url(r'^(?P<pk>\d+)/delete/', permission_required("goods.delete_good")\
        (GoodDelete.as_view()), name="goods_delete"),
    url(r'^(?P<pk>\d+)/rss/$', RssGoodsListFeed(), name = "goods_feed_rss"),
    url(r'^(?P<pk>\d+)/atom/$', AtomGoodsListFeed(), name = "goods_feed_atom"),
]
