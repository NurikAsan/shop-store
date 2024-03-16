from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularSwaggerView, SpectacularRedocView,SpectacularAPIView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('api/', SpectacularAPIView.as_view(), name="schema"),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
