from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),  # 127.0.0.1/accounts
    path('', include('tourist_info.urls')),  # Ensure this matches your app name
    path('admin/', admin.site.urls),
   ]


urlpatterns += staticfiles_urlpatterns()

# Media files handling
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
