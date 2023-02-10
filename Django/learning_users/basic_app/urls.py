from django.conf.urls import url
from basic_app import views


#Templates urls!

app_name = 'basic_app'

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    #Coding by haithem
    url(r'^user_login/$',views.user_login,name='user_login'),
    #url(r'^login/$', views.login_page, name='login'),
    #url(r'^logout/$', views.logout_request, name='logout'),
]



