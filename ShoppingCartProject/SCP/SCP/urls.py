"""SCP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from testapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index_view),
    path('add/', views.additem_view),
    path('display/',views.display_items_view),
    path('index1/',views.index1_view),
    path('homeauth/',views.home_page_view),
    path('java/',views.java_page_view),
    path('python/',views.python_page_view),
    path('aptitude/',views.aptitude_page_view),
    path('logout/',views.logout_view),
    path('signup/',views.signup_view),
    path('accounts/',include('django.contrib.auth.urls')),
    path('emp/',views.retrieve_view),
    path('insert/',views.insert_view),
    path('delete/<int:id>/',views.delete_view),
    path('update/<int:id>/',views.update_view),
]
