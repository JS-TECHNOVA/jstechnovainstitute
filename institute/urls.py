from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap


sitemaps = {
    "static": StaticViewSitemap,
}

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("get-in-touch/", views.SubmitGetInTouchForm.as_view(), name="SubmitGetInTouchForm"), 
    path("about/", views.AboutView.as_view(), name="about"), 
    path("book-demo-class/", views.BookDemoClass.as_view(), name="BookDemoClass"), 
    path("tutors/", views.Tutors.as_view(), name="tutors"),

         path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
]
