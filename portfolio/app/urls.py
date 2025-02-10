from django.urls import path
from . import views

app_name = 'app'


urlpatterns = [ path('', views.home_page, name='home_page'),
               path('contact', views.contact_function, name='contact'),
               path('project', views.my_project, name='project')
] 