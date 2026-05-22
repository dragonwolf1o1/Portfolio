from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("portfolio.urls")),
]

handler404 = "portfolio.views.error_404"
handler500 = "portfolio.views.error_500"
