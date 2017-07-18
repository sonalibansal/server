"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from solid_i18n.urls import solid_i18n_patterns
from nyaaya_web import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('nyaaya_api.urls')),
    url(r'^', include('nyaaya_web.urls')),
]
urlpatterns += solid_i18n_patterns(
     url(r'^law-explainers/$', views.law_explainers, name='law-explainers'),
     url(r'^(?P<toc_slug>[\-a-z0-9].+)/$', views.apps, name='app_page'),
     
 )