from django.urls import path
from .views import *

#-----------------------------------------------------------------------------------------------------------------------------------------------

urlpatterns = [
    
    path('list', ChatList.as_view(), name='listchat'),
    path('createchat', ChatCreate.as_view(template_name="BlogChat/createchat.html"), name='createchat'),

]