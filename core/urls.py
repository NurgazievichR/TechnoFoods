"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from debug_toolbar.toolbar import debug_toolbar_urls


schema_view = get_schema_view(
   openapi.Info(
      title="Inventory Management System",
      default_version='v1',
      description="simple product inventory management system",
      contact=openapi.Contact(email="zr121@auca.kg"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

apipatterns = [
    path('', include('apps.products.urls')),
    path('cases/', include('apps.cases.urls')),
    path('applications/', include('apps.applications.urls')),
    path('promocodes/', include('apps.promocodes.urls')),
]

docpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(apipatterns)),
    path('', include(docpatterns)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + debug_toolbar_urls()