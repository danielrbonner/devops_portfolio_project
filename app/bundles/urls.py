from django.urls import path
from bundles import views as bundles_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('api/bundles/index/', bundles_views.index, name='bundles index'),
    # path('', bundles_views.index.as_view(), name='bundles'),
    path('api/bundles/', bundles_views.bundle_list),
    path('api/bundles/<int:pk>/', bundles_views.bundle_detail),
    path('api/bundles/open/', bundles_views.bundle_list_open)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
