from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # url(r'^$',views.index,name = 'index'),
    # url(r'^search/', views.search, name='search_results'),
    # url(r'^login/', views.login, name='login'),
    # url(r'^instagram/',views.search)
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
