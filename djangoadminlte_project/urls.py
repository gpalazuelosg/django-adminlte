
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include(('core_app.urls','core_app'), namespace='core_app')),
    path('city_history/', include(('city_history.urls','city_history'), namespace='city_history')),
    
    path('admin/', admin.site.urls),
]
