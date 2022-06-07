from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static

#-----------------------------------------------------------------------------------------------------------------------------------------------

urlpatterns = [

    path('register', register, name='register'),
    path('login', login_request, name='login'),
    
    path('logout', LogoutView.as_view(template_name="BlogLogin/logout.html"), name='logout'),

    path('profile/<user_id>', profile, name='profile'),
    path('listuser', UserList.as_view(template_name="BlogLogin/listuser.html"), name='listuser'),
    path('changepass', change_password, name='changepasswd'),
    path('editprofile', UserUpdate.as_view(template_name="BlogLogin/updateuser.html"), name='update_user'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)