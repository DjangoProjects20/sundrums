from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('sundrums_admin.urls')),
    path(r'robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain'),name='robots.txt'),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'mailer/', include('mailer.urls', namespace='mailer')),
  
]\
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)