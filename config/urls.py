from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView
from rest_framework.authtoken.views import obtain_auth_token
from django.utils.translation import ugettext_lazy as _
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import GenericSitemap
from config.sitemaps import  StaticViewSitemap


sitemaps = {
    'static': StaticViewSitemap,
    # 'product':GenericSitemap({
    #     'queryset': Product.objects.all(),
    #     'date_field': 'updated',
    #     'issued_date': 'issued',
    # }, priority=0.9),
    # 'posts':GenericSitemap({
    #     'queryset': Post.objects.all_posts(),
    #     'date_field': 'updated',
    #     'pub_date': 'pub_date',
    # }, priority=0.9),
    # 'career':GenericSitemap({
    #     'queryset': Career.objects.all(),
    #     'date_field': 'updated',
    # }, priority=0.9),
}


urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # path('likes/', include('likes.urls')),

    # ADMIN SKIN
    path('jet/dashboard/', include('jet.dashboard.urls', namespace='jet-dashboard')),
    path('jet/', include('jet.urls', namespace='jet')),


    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path(
        "about/", TemplateView.as_view(template_name="pages/about.html"), name="about"
    ),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path("users/", include("shooze.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    # Your stuff: custom urls includes go here
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    # Static file serving when using Gunicorn + Uvicorn for local web socket development
    urlpatterns += staticfiles_urlpatterns()

# API URLS
urlpatterns += [
    # API base url
    path("api/", include("config.api_router")),
    # DRF auth token
    path("auth-token/", obtain_auth_token),
]

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns

admin.site.site_header = 'SHOOZE STORE'