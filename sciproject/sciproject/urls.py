"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from exam.urls import router
from exam import views

urlpatterns = [
    path('admin/', admin.site.urls),

    
    path(r'api/', include(router.urls)),
    path('', views.LacListView, name='LacListView'),
    path('Download/', views.SubjectListView, name='SubjectListView'),
    path('jso/', views.jo, name='json'),
    path('oauth/', include('social_django.urls', namespace='social')),
    path(r'logout/', auth_views.logout, {'next_page': '/'}, name='logout'),
    path('export/', views.export, name='export'),
    path('saved/', views.saved, name='saved'),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
