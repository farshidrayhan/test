"""django_site URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings # settings imported cause the original settings were changed
from django.conf.urls.static import static
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^iDTI-ESBoost/', include('music.urls')),
    url(r'^ajax/', include('ajax_test.urls')),

    # url(r'', include('music.urls')),
    # url(r'', include('music.urls')),
]

# images are stored in project folder in debug mode for non debug mode is not defined yet
if settings.DEBUG:
    urlpatterns +=  static(settings.STATIC_URL, document_root= settings.STATIC_ROOT )
    urlpatterns +=  static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT )

