from django.urls import path, include


urlpatterns = [
    # /api/user - routes
    path('api/', include(('accounts.urls', 'accounts'))),
    # /api/game - routes
    path('api/', include('rpsgame.urls'))
    
]
