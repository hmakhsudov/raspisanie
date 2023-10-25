"""
URL configuration for sovaraspisanie project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from raspisanie.views import RaspisanieView
from raspisanie.views import GroupsView, GroupScheduleView


#Указываем все ссылки на страницы
urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('site_auth.urls')),
    path('', RaspisanieView.as_view(), name="main"),
    path('groups/', GroupsView.as_view(), name="groups"),
    path('search_groups/', GroupsView.as_view(), name="search_groups"),
    path('groups/', GroupsView.as_view(), name='groups'),

    path('raspisanie/<str:group_number>/', RaspisanieView.as_view(), name='raspisanie'),
    path('group_schedule/<str:group_number>/', GroupScheduleView.as_view(), name='group_schedule'),

]