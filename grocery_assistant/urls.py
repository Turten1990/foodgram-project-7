"""grocery_assistant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import handler404, handler500
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.flatpages import views
from django.contrib.flatpages.views import flatpage
from django.urls import include, path

handler404 = "recipes.views.page_not_found"  # noqa
handler500 = "recipes.views.server_error"  # noqa

flatpages_urls = [
    path('', flatpage, {'url': '/author/'}, name='about_author'),
    path('', flatpage, {'url': '/tech/'}, name='about_tech'),
]

urlpatterns = [
    path('auth/', include('users.urls')),
    path('admin/', admin.site.urls),
    path('', include('recipes.urls')),
    path('api/', include('api.urls')),
    path('about/', include(flatpages_urls)),
    # path('auth/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    import debug_toolbar

    urlpatterns += (path("__debug__/", include(debug_toolbar.urls)),)