from django.contrib import admin

from django.urls import path, include                  # 修正

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('djoser.urls')),      # 追加
    path('api/v1/auth/', include('djoser.urls.jwt')),  # 追加
    path('api/v1/', include('apiv1.urls')),            # 追加
]
