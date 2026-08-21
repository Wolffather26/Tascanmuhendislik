from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include, path
from website.views import robots_txt, sitemap_xml


urlpatterns = [
    path("admin/", admin.site.urls),
    path("i18n/", include("django.conf.urls.i18n")),
    path("robots.txt", robots_txt, name="robots_txt"),
    path("sitemap.xml", sitemap_xml, name="sitemap_xml"),
    path("", include("website.urls")),
]
