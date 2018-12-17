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
from django.contrib.auth.decorators import login_required
from imagepool.views import get_list, upload_file, delete_file

urlpatterns = [
    url(r'^$', login_required(get_list), name = "imagepool_index"),
    url(r'^upload/$', login_required(upload_file), name = "imagepool_upload"),
    url(r'^(?P<pk>\d+)/delete/$', login_required(delete_file), name = "imagepool_delete"),
]
