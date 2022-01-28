from django.urls import path
from items import views as item_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('api/items/index/', item_views.index),
    # path('', item_views.index.as_view(), name='items'),
    path('api/items/', item_views.item_list),
    path('api/items/<int:pk>/', item_views.item_detail),
    path('api/items/open/', item_views.item_list_open)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
