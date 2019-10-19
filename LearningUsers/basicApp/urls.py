from django.conf.urls import url
from basicApp import views


app_name = 'basicApp'


urlpatterns = [
     url('register/',views.register,name='register'),
     url('user_login/',views.user_login,name='user_login'),

]
