"""hack URL Configuration

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
from django.conf.urls.static import static
from django.urls import path, re_path, include
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView
)

from main.admin import admin_site, full_admin_site
from main.views.user import CustomTokenObtainView, RegistrationView
from med.urls import router

urlpatterns = [
    path('', admin_site.urls),
    path('admin/', full_admin_site.urls),

    re_path(r'^api/', include(router.urls)),
    re_path(r'^api/registration/', RegistrationView.as_view(), name='registration'),
    re_path(r'^api/token/$', CustomTokenObtainView.as_view(), name='token_obtain_pair'),
    re_path(r'^api/token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
    re_path(r'^api/token/verify/$', TokenVerifyView.as_view(), name='token_verify'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
                   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
