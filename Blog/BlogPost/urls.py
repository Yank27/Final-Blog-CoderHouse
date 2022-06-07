from django.urls import path
from .views import *
from django.conf.urls.static import static

#-----------------------------------------------------------------------------------------------------------------------------------------------

urlpatterns = [
    
    path('addpost', BlogCreate.as_view(template_name="BlogPost/createpost.html"), name='createpost'),
    path('list', BlogList.as_view(), name='listpost'),
    path('post/<pk>', BlogDetail.as_view(template_name="BlogPost/detailpost.html"), name='detail_post'),
    path('post/update/<pk>', BlogUpdate.as_view(template_name="BlogPost/updatepost.html"), name='update_post'),
    path('post/delete/<pk>', BlogDelete.as_view(template_name="BlogPost/post_confirm_delete.html"), name='delete_post'),
    path('search/', search, name="search"),


]