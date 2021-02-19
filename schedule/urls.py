from django.conf.urls import url

from . import views
urlpatterns = [

    url(r'^register_interview_shceduling/$', views.scheduling),
    url(r'^time_slot_matching/$', views.time_slot_matching),
    ]