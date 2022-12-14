from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="My service API",
      default_version='v1',
      description=" My description",
      terms_of_service="https://www.mysite.com/policies/terms/",
      contact=openapi.Contact(email="my_contact@snippets.local"),
      license=openapi.License(name="My License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include('api.urls')),
    path('orders/', include('orders.urls')),
    path('users/', include('users.urls')),
]
