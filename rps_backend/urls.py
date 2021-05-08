from django.urls import path, re_path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # /api/user - routes
    path('api/', include(('accounts.urls', 'accounts'))),
    # /api/game - routes
    path('api/', include('rpsgame.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# React routes, back to index.html
urlpatterns += [
    path('login', TemplateView.as_view(template_name='index.html')),
    path('signup', TemplateView.as_view(template_name='index.html')),
    path('play', TemplateView.as_view(template_name='index.html')),
    path('profile', TemplateView.as_view(template_name='index.html')),
    path('', TemplateView.as_view(template_name='index.html')),
]
