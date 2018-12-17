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
from django.contrib.auth.views import login, logout
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from about.views import AboutView
from contacts.views import ContactsView
from howtobuy.views import HowToBuyView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', login, name="login"),
    url(r'^logout/', logout, name="logout"),
    url(r'^', include('main.urls')),
    url(r'^guestbook/', include('guestbook.urls')),
    url(r'^news/', include('news.urls')),
    url(r'^imagepool/', include('imagepool.urls')),
    url(r'^categories/', include('categories.urls')),
    url(r'^goods/', include('goods.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^about/', AboutView.as_view(), name = "about"),
    url(r'^contacts/', ContactsView.as_view(), name = "contacts"),
    url(r'^howtobuy/', HowToBuyView.as_view(), name = "howtobuy"),
]   

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
