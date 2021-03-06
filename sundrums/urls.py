from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.generic import TemplateView
from sundrums_admin.sitemaps import *
from django.contrib.sitemaps.views import sitemap
from sundrums_admin import views
#dicthonari for posts
sitemaps = {
    'Post_categories' : Post_categoriesSitemap,
    'Posts' : PostsSitemap,
    'tipe_product' : tipe_productSitemap,
    'tipe_kurs'  : tipe_kursSitemap,
}



urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('sundrums_admin.urls')),
    path('sitemap.xml',sitemap, {'sitemaps':sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^posts/(?P<post_id>\w+)/', views.one_categories, name='posts'),
    url(r'^post_categories/(?P<post_id>\w+)/', views.one_categories, name='post_categories'),
    
    #тестирую ссылки первого уровня для переxода на главные ветки
   url(r'^magazin/$', views.tipe_posts_magazin, name='magazin'),
   url(r'^entsiklopediia/$', views.tipe_posts_entsiklopediia, name='entsiklopediia'),
   url(r'^novosti/$', views.tipe_posts_novosti, name='novosti'),
   url(r'^sobytiia/$', views.tipe_posts_sobytiia, name='sobytiia'),
   url(r'^korporativnye-treningi/$', views.tipe_posts_korporativnye_treningi, name='korporativnye-treningi'),
   url(r'^shkola/$', views.tipe_posts_shkola, name='shkola'),
   url(r'^faq/$', views.tipe_posts_FAQ_page, name='faq'),
   #тестирую ссылки первого уровня
      #тестирую ссылки второго уровня
   url(r'^magazin/(?P<slug>.+)/$', views.one_post_simple, name='magazin'),
   url(r'^entsiklopediia/(?P<slug>.+)/$', views.one_post_simple, name='entsiklopediia'),
   url(r'^novosti/(?P<slug>.+)/$', views.one_post_simple, name='novosti'),
   url(r'^sobytiia/(?P<slug>.+)/$', views.one_post_simple, name='sobytiia'),
   url(r'^korporativnye-treningi/(?P<slug>.+)/$', views.one_post_simple, name='korporativnye-treningi'),
   url(r'^shkola/(?P<slug>.+)/$', views.one_post_simple, name='shkola'),
   url(r'^faq/(?P<slug>.+)/$', views.one_post_simple, name='faq'),
   #тестирую ссылки второго уровня
   url(r'^kursi/(?P<slug>.+)/', views.tipe_kurs_page, name='kursi'),
   #url(r'^product_page/(?P<product_id>\w+)/', views.tipe_product_page, name='product_page'),
   url(r'^serteficat/(?P<slug>.+)/', views.tipe_product_page, name='serteficat'),
    
   
   
   
    path(r'robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain'),name='robots.txt'),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'mailer/', include('mailer.urls', namespace='mailer')),
  
]\
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)