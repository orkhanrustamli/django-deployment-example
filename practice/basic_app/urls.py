from django.conf.urls import url
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    url(r'^%', views.index, name='index'),
    url(r'^registration$', views.register, name='register'),
    url(r'^user_login', views.user_login, name='user_login'),
    url(r'^user_logout', views.user_logout, name='user_logout'),
]
