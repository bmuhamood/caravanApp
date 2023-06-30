from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.views.i18n import set_language

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('contact_us/', include('contact.urls')),
    path('set-language/', set_language, name='set_language'),
    path('products/dashboard/', TemplateView.as_view(template_name='dashboard.html'), name='dashboard'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
