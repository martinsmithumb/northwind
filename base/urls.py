from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler403, handler404, handler500


urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('customers/', include('customers.urls')),
    path('employees/', include('employees.urls')),
    path('orders/', include('orders.urls')),
    path('', include('pages.urls')),
    path('products/', include('products.urls')),
    path('shippers/', include('shippers.urls')),
    path('suppliers/', include('suppliers.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]

handler403 = 'base.views.error_403_view'
handler404 = 'base.views.error_404_view'
handler500 = 'base.views.error_500_view'