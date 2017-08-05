from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.ProductList.as_view(), name='product_list'),
    url(r'^dashboard/users/$', views.UserList.as_view(), name='dashboard_user_list'),
    url(r'^dashboard/users/(?P<pk>\d+)/addtostaff$', views.UserAddToStaff.as_view(), name='dashboard_user_addtostaff'),
    url(r'^dashboard/users/(?P<pk>\d+)/removefromstaff$', views.UserRemoveFromStaff.as_view(), name='dashboard_user_removefromstaff'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)