from django.urls import path

from . import views

app_name = 'sample_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('example', views.example, name='example'),
    path('send-sms', views.send_sms, name='send_sms'),
]
