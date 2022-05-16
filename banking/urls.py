
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework import routers
from thirdparty import views
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'customers', views.CustomerView, 'customer')
router.register(r'customer_groups', views.CustomerGroupView, 'customer_group')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('thirdparty/api/', include("thirdparty.urls")),
    path('safemanager/',include('safemanager.urls')),
    path('safemanager/manageuser/',include('usermanagement.urls')),
    path('safemanager/manageuser/',include("django.contrib.auth.urls"))
] 

if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  