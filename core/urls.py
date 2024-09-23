from django.contrib import admin
from django.http import HttpResponse
from django.urls import re_path, path, include
from django.conf.urls.static import static
from django.conf import settings
from django.shortcuts import redirect

# External packages urls
urlpatterns = [
    path("rosetta/", include("rosetta.urls")),
]

# Custom urls
urlpatterns += [
    path("", include("apps.website.urls")),
]

# Admin urls
urlpatterns += [
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
