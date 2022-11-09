from django.urls import path
from .import views
app_name = 'myapp1'

urlpatterns = [
    path('',views.index, name='index'),
    path('register/',views.register, name='register'),
    path('login/',views.login, name='login'),
    path('home/<int:id>',views.home, name='home'),
    path('changepass/<int:id>',views.changepass, name='changepass'),
    path('update/<int:id>',views.update, name='update'),
    path('logout/',views.logout, name='logout'),
    path('gallery/',views.gallery, name='gallery'),
    path('view_details/<int:id>',views.view_details, name='view_details'),
]